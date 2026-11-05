#!/usr/bin/env python3
"""Make two true full-viewport, inline-looping WebP demonstrations from OCTV MP4 captures.

All frames are sampled from the recorded full browser viewport. No zoom, crop,
screenshot patchwork, overlays, generated UI, or individual component cut-outs.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets" / "01-octv"
STORIES = [
    (
        "opt_full_cctv_overview.webp",
        ["demo_cctv.mp4", "demo_overview.mp4"],
    ),
    (
        "opt_full_analysis_routes.webp",
        ["demo_analysis.mp4", "demo_routes.mp4"],
    ),
]
FRAME_WIDTH = 1080
FRAME_RATE = 5
MAX_FRAMES_PER_CLIP = 50
FRAME_DURATION_MS = 230
WEBP_QUALITY = 59


def run(args):
    proc = subprocess.run(args, text=True, capture_output=True, check=True)
    return proc.stdout


def video_info(path):
    info = json.loads(run([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height:format=duration",
        "-of", "json", str(path),
    ]))
    stream = info["streams"][0]
    width, height = int(stream["width"]), int(stream["height"])
    duration = float(info.get("format", {}).get("duration") or 0)
    if width < 1000 or height < 700 or width / height < 1.3:
        raise ValueError(f"Source does not show a full desktop viewport: {path}: {width}x{height}")
    print(f"SOURCE {path.name}: {width}x{height}, {duration:.2f}s, {path.stat().st_size:,} bytes", flush=True)
    return width, height, duration


def evenly_sample(items, limit):
    if len(items) <= limit:
        return items
    return [items[round(i * (len(items) - 1) / (limit - 1))] for i in range(limit)]


def sampled_frames(path, destination, target_size):
    destination.mkdir(parents=True, exist_ok=True)
    pattern = destination / "frame_%05d.png"
    run([
        "ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(path), "-vf",
        f"fps={FRAME_RATE},scale={target_size[0]}:{target_size[1]}:flags=lanczos",
        "-vsync", "vfr", str(pattern),
    ])
    candidates = sorted(destination.glob("frame_*.png"))
    if len(candidates) < 2:
        raise RuntimeError(f"No usable video frames: {path}")
    kept = evenly_sample(candidates, MAX_FRAMES_PER_CLIP)
    frames = []
    for frame_path in kept:
        with Image.open(frame_path) as f:
            frames.append(f.convert("RGB"))
    print(f"SAMPLE {path.name}: {len(candidates)} -> {len(frames)} genuine uncropped frames", flush=True)
    return frames


def build_story(output, sources):
    meta = [video_info(SOURCE_DIR / src) for src in sources]
    ratios = [w / h for w, h, _ in meta]
    if max(ratios) - min(ratios) > 0.02:
        raise ValueError("Cannot join clips with inconsistent full-screen aspect ratios.")
    first_width, first_height, _ = meta[0]
    width = FRAME_WIDTH
    height = max(2, round(width * first_height / first_width / 2) * 2)
    frames = []
    with TemporaryDirectory() as tmp:
        for n, src in enumerate(sources):
            frames.extend(sampled_frames(
                SOURCE_DIR / src,
                Path(tmp) / f"part{n}",
                (width, height),
            ))
    if len(frames) < 4:
        raise RuntimeError("Not enough frames to preserve the two recorded workflows")
    target = SOURCE_DIR / output
    frames[0].save(
        target, format="WEBP", save_all=True, append_images=frames[1:],
        duration=FRAME_DURATION_MS, loop=0, quality=WEBP_QUALITY,
        method=5, lossless=False,
    )
    with Image.open(target) as saved:
        if saved.n_frames < 2 or saved.size != (width, height):
            raise RuntimeError(f"Encoded WebP verification failed: {target}")
        encoded_frames = saved.n_frames
    print(
        f"OUTPUT {output}: {width}x{height}, {len(frames)} actual samples / {encoded_frames} encoded frames, "
        f"{len(frames) * FRAME_DURATION_MS / 1000:.1f}s loop, "
        f"{target.stat().st_size:,} bytes",
        flush=True,
    )


if __name__ == "__main__":
    for file_name, clips in STORIES:
        build_story(file_name, clips)
