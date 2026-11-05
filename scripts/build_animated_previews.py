#!/usr/bin/env python3
"""Generate small, looping README animations from original captured GIFs."""
from pathlib import Path
from PIL import Image, ImageSequence

SPECS = [
    ("assets/01-octv/01_cctv_detection.gif", "assets/01-octv/opt_cctv_detection.webp", 960, 6, 68),
    ("assets/01-octv/02_incident_analysis.gif", "assets/01-octv/opt_incident_analysis.webp", 960, 6, 68),
    ("assets/01-octv/03_agency_routes.gif", "assets/01-octv/opt_agency_routes.webp", 960, 6, 68),
    ("assets/02-gooddeedquest/01_community_algorithm.gif", "assets/02-gooddeedquest/opt_community_algorithm.webp", 380, 8, 73),
    ("assets/02-gooddeedquest/02_team_challenge_llm.gif", "assets/02-gooddeedquest/opt_team_challenge_llm.webp", 380, 8, 73),
    ("assets/03-climbing-web/01_gym_map_search.gif", "assets/03-climbing-web/opt_gym_map_search.webp", 900, 6, 70),
    ("assets/03-climbing-web/02_gym_recommend.gif", "assets/03-climbing-web/opt_gym_recommend.webp", 900, 6, 70),
    ("assets/03-climbing-web/03_results_chart_players.gif", "assets/03-climbing-web/opt_results_chart_players.webp", 900, 6, 70),
]

def convert(source, destination, max_width, fps, quality):
    source = Path(source)
    destination = Path(destination)
    frame_ms = 1000.0 / fps
    frames = []
    elapsed = 0.0
    next_sample = 0.0
    with Image.open(source) as im:
        w, h = im.size
        factor = min(1.0, max_width / w)
        target_size = (max(1, round(w * factor)), max(1, round(h * factor)))
        for gif_frame in ImageSequence.Iterator(im):
            duration = float(gif_frame.info.get("duration") or 100)
            duration = max(20.0, duration)
            end = elapsed + duration
            if next_sample < end:
                frame = gif_frame.convert("RGB")
                if frame.size != target_size:
                    frame = frame.resize(target_size, Image.Resampling.LANCZOS)
                while next_sample < end:
                    frames.append(frame)
                    next_sample += frame_ms
            elapsed = end
    if len(frames) < 2:
        raise RuntimeError(f"Not enough frames in {source}: {len(frames)}")
    frames[0].save(destination, format="WEBP", save_all=True, append_images=frames[1:],
                   duration=round(frame_ms), loop=0, quality=quality, method=4, lossless=False)
    with Image.open(destination) as check:
        if getattr(check, "n_frames", 1) < 2:
            raise RuntimeError(f"Animation verification failed: {destination}")
        output_frames = check.n_frames
    original_size = source.stat().st_size
    compressed_size = destination.stat().st_size
    if compressed_size >= original_size:
        raise RuntimeError(f"File size did not improve: {source}, {compressed_size} >= {original_size}")
    print(f"{source}: {original_size:,} -> {compressed_size:,} B "
          f"({100 * (1 - compressed_size / original_size):.1f}% smaller); "
          f"{len(frames)} input samples; {output_frames} output frames; {target_size}", flush=True)
    return original_size, compressed_size

def main():
    original, compressed = 0, 0
    for spec in SPECS:
        before, after = convert(*spec)
        original += before
        compressed += after
    print(f"ALL 8: {original:,} -> {compressed:,} B; "
          f"{100 * (1 - compressed / original):.1f}% smaller", flush=True)

if __name__ == "__main__":
    main()
