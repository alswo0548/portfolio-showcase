# 포트폴리오 인수인계 검수 — 2026-11-05

## 반영 기록

- 인수 시 main: `0bde09db33a76f118bdd97a5967b1c018f1ea9c3` (PR #2까지 반영)
- 기존 작업 PR #3: `fix/portfolio-media-and-octv-20261104`, head `7da01fc`
- PR #3 병합 완료: `4dd14dd1333638fd7408e0e1b9e5b41e1ef6ee14`
- 추가 작업: `fix/portfolio-final-20261105` — 정적 영상 플레이어와 소개 문서 링크

## 확인한 결과

- GitHub 비로그인 브라우저에서 표지 3개, OCTV 소개 이미지 5개, GoodDeedQuest 2개, Climbing Web 7개 모두 로딩 확인.
- 기존 MP4 GitHub blob 페이지에는 플레이어가 없고 View raw만 표시됨. 별도의 정적 플레이어를 추가한 이유.
- 새 플레이어의 실제 브라우저에서 MP4 9개 재생: `readyState=4`, `paused=false`, 재생 시간 증가 확인.
- 모든 MP4: H.264/yuv420p, ffmpeg 전체 디코딩 오류 0.
- 초기 플레이어의 video src 없음, readyState=0. 버튼 클릭 시 선택 영상만 설정.
- 390px iframe(스크롤바 제외 콘텐츠 폭 375px)에서 세 프로젝트 대표 영상 재생과 가로 넘침 없음 확인. 실제 휴대폰 Safari/Chrome 검증은 수행하지 않음.
- 첨부 기획 원본의 서비스 워크플로우·학습 워크플로우·ERD와 보관 이미지의 픽셀이 일치함. 시스템 아키텍처 첨부 PNG는 일부 잘림이 있어 기존 확보본 보존.
- OCTV 원본의 LangGraph 노드·FastMCP 프로세스 내 호출·위험도 규칙·알림 재시도·Compose를 연결 도구로 재확인. 서비스·서버·DB 변경 없음.

## 소개 페이지 시연 이미지 용량

| 프로젝트 | 기존 GIF 합계 | JPG 미리보기 합계 | 감소 |
|---|---:|---:|---:|
| OCTV | 14,279,458 B | 559,785 B | 96.1% |
| GoodDeedQuest | 6,294,556 B | 253,431 B | 96.0% |
| Climbing Web | 15,568,349 B | 536,639 B | 96.6% |

위 값은 시연 이미지 파일 합계이며 네트워크 로딩 시간이나 페이지 전체 전송량 측정값이 아님.

## 공개 배포 및 전환 검수

- 기존 PR #4 병합 `70a7f3b`, 새 저장소의 초기 파일 트리 SHA `2db23a73e5912a03ffedc54d6c7553e7c47571a4`와 동일함을 확인.
- 새 저장소 `alswo0548/portfolio-showcase` PR #1 병합 `978257e`. GitHub Pages main / root 활성화.
- 공개 Pages에서 영상 9개 모두 실제 재생 시간 증가, readyState=4, 미디어 오류 없음 확인. 로컬 성공만으로 판단하지 않음.
- 새 저장소 비로그인 메인 표지 3개 및 OCTV 상세 이미지 5개, GoodDeedQuest 2개, Climbing Web 7개 정상 표시. Contributors는 alswo0548 1명, Claude 미표시.
- 기존 저장소에는 Contributors의 Claude 표시가 남아 있으므로 제거 완료라고 보고하지 않음. 기존 이력과 주소는 보존하고 PR #5로 새 주소 안내 추가.
- HTML 갱신 후 구버전 JavaScript가 브라우저 캐시에 남는 현상을 확인해 script URL에 버전 추가.

## 남은 제한

- OCTV 모바일 실제 실행 캡처 2장 제공받아 추가. 영상·푸시 수신·내비게이션 실행은 미검증.
- 390px 웹 플레이어 검수는 로컬 iframe 기준. 실제 휴대폰 Safari/Chrome 및 GitHub README 자체의 휴대폰 화면은 미검증.
- 파일 용량 감소는 확인했으나 이용자별 회선에서 몇 초 이내 표시된다고 보장하지 않음.


## 2026-11-05 추가 보정 — OCTV 전체 웹 화면 자동재생

- **원인:** 기존 OCTV 표시 GIF는 특정 기능 영역을 잘라낸 화면이어서, 상세페이지에서 웹 전체 구조(좌측 메뉴·상단·페이지 컨텍스트)가 보이지 않았다. 단순 GIF→WebP 압축으로는 이 문제가 해결되지 않는다.
- **기준 원본:** 2026-11-04 운영 웹에서 녹화한 `demo_cctv.mp4`, `demo_overview.mp4`, `demo_analysis.mp4`, `demo_routes.mp4` 네 개 모두 영상 메타데이터 `1348×926` 확인. 각각 12.67, 7.07, 9.47, 14.33초.
- **수정 방식:** 원본의 전체 프레임을 유지하고 두 순서형 이야기로 재구성. 첫 번째는 CCTV→통합관제, 두 번째는 위험도→대응기관·경로. 특정 화면 부분을 잘라내지 않으며, 일부 프레임 간격 추출로 재생 구간이 압축되었다.
- **인코딩:** `scripts/build_octv_fullscreen_previews.py`. 결과 1080×742, 무한 반복 애니메이션 WebP. `opt_full_cctv_overview.webp` 1,574,132바이트/83개 인코딩 프레임/19.6초, `opt_full_analysis_routes.webp` 1,596,484바이트/94개 인코딩 프레임/22.3초.
- **동작 검증:** GitHub Actions [성공 실행 #41980700394](https://github.com/alswo0548/portfolio-showcase/actions/runs/41980700394)에서 네 원본의 해상도와 애니메이션 프레임 수·출력 크기 검증. GitHub 상세 README에는 두 개의 `<img src="...opt_full_...webp">`만 삽입하고 기존 부분 화면 GIF 이미지는 제거.
- **크기 비교:** 기존 OCTV 표시 GIF 3개 합계 14,279,458바이트 → 새 화면 전체 시연 2개 합계 3,170,616바이트(77.8% 감소). 이 수치는 페이지 전체 전송량이나 실제 네트워크 시간은 아니다.
- **공개 브라우저 검증:** PR #5 병합 이후 [GitHub Actions Chromium 실측 QA #41981858575](https://github.com/alswo0548/portfolio-showcase/actions/runs/41981858575)가 성공했다. 비로그인 GitHub OCTV README에서 데스크톱 1440px 및 모바일 폭 390px 각각 두 WebP의 로딩·실제 프레임 변화(스크린샷 해시 변경)·화면 내 표시를 검증했다. 두 자산 모두 실제 크기 1080×742, 데스크톱 표시 폭 1012px, 모바일 표시 폭 324px으로 확인됐다. 이 결과는 Chromium 기준이며 Safari·사용자별 회선의 초기 로딩 시간은 별도로 측정하지 않았다.
