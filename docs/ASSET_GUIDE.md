# 이미지 · 시연 영상 관리 규칙

포트폴리오의 모든 이미지는 이 저장소의 `assets/` 폴더 한 곳에서 관리합니다.
프로필 README(`alswo0548/alswo0548`)도 이 폴더의 파일을 주소로 불러오므로, **파일을 교체하면 프로필과 소개 페이지가 함께 바뀝니다.**

## 폴더 구조

```text
assets/
├── 01-octv/
│   ├── thumbnail.png          # 프로필·목록 카드 이미지 (1280×640)
│   ├── erd.png                # 초기 설계 ERD (2026-10-02)
│   ├── 01_cctv_detection.gif   # 기존 실제 웹 촬영본의 연속 CCTV 구간
│   ├── 02_incident_analysis.gif # 운영 웹 사건 분석 (2026-11-04)
│   ├── 03_agency_routes.gif     # 운영 웹 경로 비교 (2026-11-04)
│   └── screens/               # 실제 운영 화면 JPG, 계정 영역 크롭
│       ├── overview.jpg
│       ├── incidents.jpg
│       ├── routes.jpg
│       └── delivery.jpg
├── 02-gooddeedquest/
│   ├── thumbnail.png
│   ├── 01_community_algorithm.gif   # 소개 페이지 시연 GIF
│   ├── 01_community_algorithm.mp4   # 같은 장면의 고화질 영상
│   ├── 01_community_algorithm.png   # 대표 장면 정지 이미지
│   ├── 02_team_challenge_llm.gif
│   ├── 02_team_challenge_llm.mp4
│   └── 02_team_challenge_llm.png
└── 03-climbing-web/
    ├── thumbnail.png
    ├── 01_gym_map_search.gif        # 지도 검색 · 로드뷰 · 날씨 시연
    ├── 02_gym_recommend.gif         # 성향 설문 추천 시연
    ├── 03_results_chart_players.gif # 선수 기록 차트 → 선수 상세 시연
    ├── (같은 이름의 .mp4 · .png)
    └── screens/                     # 실행 화면 스크린샷 (1440px 폭 JPG)
        ├── main.jpg
        ├── disciplines.jpg
        ├── players.jpg
        └── results.jpg
```

## 파일명 규칙

| 종류 | 규칙 | 예시 |
|---|---|---|
| 프로젝트 폴더 | `순서 두 자리-영문 소문자-하이픈` | `01-octv`, `03-climbing-web` |
| 썸네일 | 항상 `thumbnail.png` | `assets/01-octv/thumbnail.png` |
| 시연 GIF | `순서 두 자리_기능명.gif` (영문 소문자 · 밑줄) | `02_team_challenge_llm.gif` |
| 고화질 영상 · 정지 이미지 | GIF와 같은 이름에 확장자만 `.mp4`, `.png` | `02_team_challenge_llm.mp4` |
| 스크린샷 | `screens/화면이름.jpg` | `screens/incidents.jpg` |

한글·공백이 들어간 파일명은 주소가 깨지기 쉬우니 쓰지 않습니다.

## 권장 크기

| 종류 | 크기 | 용량 목표 |
|---|---|---|
| 썸네일 | 1280×640 (2:1) PNG | 500KB 이하 |
| 모바일 앱 GIF | 폭 360~400px, 15fps | 10MB 이하 (권장 5MB 이하) |
| 웹 화면 GIF | 폭 800~960px, 10~12fps | 10MB 이하 |
| 스크린샷 | 폭 1600px JPG | 300KB 이하 |

## 시연 GIF 교체 방법

현재 OCTV는 **부분 화면 GIF를 다시 자르는 방식으로 교체하지 않습니다.** 원본 전체 웹 녹화를 보존하고, OCTV 상세에 표시되는 2개의 `opt_full_*.webp`만 교체합니다. 아래 일반 GIF 교체 설명은 다른 프로젝트의 기존 자산에도 적용됩니다.

1. 새 파일을 **같은 이름**으로 만들어 `assets/<프로젝트>/`에 덮어씁니다.
2. 커밋 후 GitHub에서 소개 페이지를 열어 바뀐 이미지를 확인합니다.
3. 프로필 화면은 GitHub 이미지 캐시 때문에 몇 분 늦게 바뀔 수 있습니다. 바로 바꾸고 싶다면 프로필 README의 이미지 주소 끝에 `?v=2` 처럼 버전을 붙입니다.

## 시연 GIF 추가 방법

1. `assets/01-octv/02_incident_analysis.gif`로 저장합니다.
2. `projects/01-octv/README.md`의 해당 **시연** 섹션에 아래 형식으로 추가합니다.

```html
<p align="center">
  <img src="../../assets/01-octv/02_incident_analysis.gif" alt="사건 상세와 위험도 분석 시연" width="100%">
</p>
```

3. GIF 바로 아래에 기능 설명 1~3문장과 **"이 장면을 보세요"** 한 줄을 적습니다.

세로로 긴 모바일 화면 GIF는 GoodDeedQuest 소개 페이지처럼 **2칸 표**로 GIF와 설명을 나란히 둡니다.
`<img align="left">` 로 띄우면 번호 목록 · 글머리 기호가 GIF 위에 겹쳐 보일 수 있으니 쓰지 않습니다.

```html
<table>
<tr>
<td width="40%" valign="top"><img width="100%" src="../../assets/02-gooddeedquest/01_community_algorithm.gif" alt="설명"></td>
<td valign="top">

**무엇을 하나요**<br>
(설명 — 표 칸 안에서도 Markdown을 쓰려면 위아래에 빈 줄을 둡니다)

</td>
</tr>
</table>
```

## 지켜야 할 원칙

- 실제로 실행한 화면만 사용합니다. 목업 화면은 **목업**이라고 표시합니다.
- 테스트 데이터로 촬영했다면 소개 페이지 하단에 그 사실을 적습니다.
- 화면에 API 키·비밀번호·실제 개인정보가 보이지 않는지 확인합니다.
- 배속·자막을 넣었다면 화면 안에 표시합니다.


## 현재 표시 방식 — 상세 README에서 빠른 애니메이션 자동 재생

GitHub 프로젝트 상세 README에는 원본 GIF에서 재인코딩한 **애니메이션 WebP**를 `<img src="...webp">`로 직접 삽입합니다. GIF와 동일하게 페이지 안에서 클릭 없이 자동 반복 재생하며, 고화질 원본 GIF·MP4는 보존합니다. 첫 애니메이션은 `loading="eager"`, 아래쪽은 `loading="lazy"`로 지정해 초기 로딩 부담을 줄입니다. 브라우저의 모션 접근성 설정에 따라 자동 재생이 차단될 수 있습니다.

- **OCTV:** 기존 전체 화면 원본 MP4 네 개에서 직접 추출한 웹 화면 전체(좌측 메뉴 포함) 애니메이션 WebP **2개** 자동 재생: `opt_full_cctv_overview.webp`(탐지→통합관제), `opt_full_analysis_routes.webp`(위험도→기관·경로). 원본 캡처 1348×926, 출력 1080×742, 각 1.57MB·1.60MB. 이전 부분 화면 GIF·WebP는 보존용으로만 둡니다.
- **GoodDeedQuest:** 커뮤니티 개인화 추천·AI 팀원 추천 애니메이션 WebP 2개 자동 재생.
- **Climbing Web:** 지도·성향 설문·선수 차트 애니메이션 WebP 3개 자동 재생.
- 원본 GIF 8개와 전체 화면 MP4 네 개는 보존합니다. 새로 표시하는 OCTV WebP 2개는 MP4 기반이며, 나머지 프로젝트의 WebP 5개는 원본 GIF 기반입니다. 상세페이지의 재생을 JPG 미리보기·클릭형 플레이어로 되돌리지 않습니다.
- 변환은 `python -m pip install Pillow` 후 `python scripts/build_animated_previews.py`로 재생성합니다. GIF 기반 애니메이션 8개의 최초 변환 결과는 36,142,363 B → 13,099,744 B(63.8% 감소)이며 프레임 수와 크기를 검증했습니다. OCTV 표시용 2개는 별도 스크립트 `scripts/build_octv_fullscreen_previews.py`로 MP4 4개에서 생성했고, 실제 GitHub Actions 성공 실행에서 1,574,132 B 및 1,596,484 B를 확인했습니다. 체감 속도는 GitHub CDN·브라우저 상태에 좌우됩니다.

고화질 MP4용 선택형 페이지(`index.html`·`demos.js`)도 `autoplay muted loop playsinline`으로 자동 재생합니다. 브라우저가 자동 재생을 차단한 경우에만 재생 버튼이 표시됩니다. 운영 서비스·DB와 통신하지 않는 정적 플레이어입니다.

기획 원본은 `assets/01-octv/design/`에 보존합니다. 기획과 구현 차이는 기술 상세 문서에 구분합니다.

## 플레이어 배포 및 수정

- GitHub Pages를 `main` 브랜치의 `/ (root)`에서 배포합니다. `.nojekyll`을 유지합니다.
- 새 영상은 `demos.js`의 목록에 등록하고 해당 ID를 소개 페이지의 링크에 연결합니다.
- 운영 서비스 API에 연결하지 않는 정적 플레이어입니다. 로그인·알림 발송·사건 생성이 없습니다.
- 저장소 이름을 바꾸거나 복사할 때는 문서의 Pages 주소와 플레이어의 GitHub 문서 주소를 함께 변경합니다.
- 배포 후 비로그인 브라우저에서 각 영상의 실제 재생과 모바일 폭을 확인합니다.
