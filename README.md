# Video Download - English

The scripts in this repository were created to simplify batch downloading of lecture videos. They read each video's URL and the desired save name from standard input (stdin) or from an input file, download them sequentially, print download progress to the console, and provide basic error handling. The scripts use only the Python standard library (urllib) and do not require external dependencies.

## Usage
The script accepts a list of videos to download via standard input (stdin). It downloads each URL sequentially and saves them locally.

### Run (PowerShell, from the current working directory)

```powershell
python .\Video_Download.py < .\Video_Download_Link.txt
# Or interactive input:
python .\Video_Download.py
# If run interactively, enter the number of videos on the first line,
# then provide URL/name pairs line by line.
```

### Input file format (example `Video_Download_Link.txt`)

```
3
https://example.com/video1.mp4
Lecture1
https://example.com/video2.mp4
Lecture2
https://example.com/video3.mp4
Lecture3
```

### Input rules
- First line: number of videos to download (positive integer)
- For each video, provide two lines: the first line is the URL, the second line is the filename to save (without extension)

## Code overview

Key components and behavior of the script:

### download_progress(block_count, block_size, total_size)
- Callback passed to `urllib.request.urlretrieve`.
- Calculates downloaded bytes and prints progress (%) and transferred MB to the console.

### save_video(video_url, save_name)
- Downloads the video at `video_url` and saves it as `save_name + ".mp4"` locally.
- By default it saves to the current working directory because any absolute download path is commented out.
    - To change the default directory, edit/enable the `download_path` string inside `save_video`, e.g. `"C:\\Users\\PSH\\Downloads\\" + save_name + ".mp4"`.
- Creates target directories as needed using `os.makedirs`.
- Error handling:
    - `urllib.error.HTTPError`: prints HTTP status and message
    - `urllib.error.URLError`: prints URL/network errors
    - `PermissionError`: prints file write permission issues
    - `OSError`: prints general filesystem errors
    - Other exceptions: prints exception type and details

### main()
- Reads the first line from stdin and parses the number of videos `N`.
- Reads `N` URL/name pairs and appends valid entries to a list; malformed entries (empty URL/name) are skipped with a warning.
- If there is at least one valid video entry, calls `save_video` sequentially for each.
- Catches and reports `ValueError`, `EOFError`, `KeyboardInterrupt`, and other top-level errors with user-friendly messages.

### Notes and recommendations
- Do not include path separators (`\` or `/`) or OS-disallowed characters in filenames; the script does not perform filename sanitization.
- Check available disk space and write permissions before downloading large files.
- The script downloads sequentially. For concurrent downloads, extend the script with multithreading or asynchronous logic.
- No external dependencies are required; the script uses `urllib` from the standard library.

### Quick tips
- Change default save directory: modify the `download_path` variable inside `save_video` to an absolute path.
- Handle filename collisions: check `os.path.exists` and append a numeric suffix to avoid overwriting existing files.

---

# Video Download - Korean

이 저장소의 스크립트는 강의 동영상을 일괄(배치)으로 손쉽게 내려받기 위해 제작되었습니다. 표준 입력(`stdin`) 또는 입력 파일로부터 각 비디오의 URL과 저장할 이름을 받아 순차적으로 다운로드하며, 다운로드 진행률을 콘솔에 출력하고 기본적인 예외 처리를 제공합니다. 별도의 외부 라이브러리 없이 파이썬 표준 라이브러리(`urllib`)만으로 동작합니다.


## 코드 사용법
이 저장소의 스크립트는 표준 입력(stdin)을 통해 다운로드할 비디오 목록을 받아, 각 URL을 순차적으로 내려받아 로컬에 저장합니다.

### 실행 방법 (PowerShell, 현재 작업 디렉터리에서)

```powershell
python .\Video_Download.py < .\Video_Download_Link.txt
# 또는 직접 입력 방식:
python .\Video_Download.py
# 실행 후 첫 줄에 비디오 개수 입력, 이후 URL/이름 쌍을 줄 단위로 입력
```

### 입력 파일 형식 (예시 `Video_Download_Link.txt`)

```
3
https://example.com/video1.mp4
Lecture1
https://example.com/video2.mp4
Lecture2
https://example.com/video3.mp4
Lecture3
```

### 입력 규칙
	- 첫 줄: 다운로드할 비디오 수 (양의 정수)
	- 그다음으로 각 비디오마다 두 줄: 첫 줄은 URL, 두 번째 줄은 저장할 파일명(확장자 없이)

## 코드 설명

스크립트 주요 구성과 동작은 다음과 같습니다.

### `download_progress(block_count, block_size, total_size)`
- `urllib.request.urlretrieve`가 호출될 때 전달되는 콜백입니다.
- 다운로드된 바이트 수를 받아 진행률(%)과 MB 단위의 전송량을 콘솔에 출력합니다.

###  `save_video(video_url, save_name)`
- 주어진 `video_url`에서 비디오를 다운로드하여 로컬에 `save_name + ".mp4"`로 저장합니다.
- 현재 코드에서는 절대 경로 부분이 주석 처리되어 있어, 기본적으로 실행 중인 작업 디렉터리에 `save_name.mp4`로 저장됩니다.
    - 원하는 디렉터리에 저장하려면 `download_path`의 주석 처리된 문자열을 수정/활성화하세요. 예: `"C:\\Users\\PSH\\Downloads\\" + save_name + ".mp4"`
- 필요한 경우 대상으로 디렉터리를 자동으로 생성합니다(`os.makedirs` 사용).
- 예외 처리:
    - `urllib.error.HTTPError`: HTTP 응답 오류 (상태 코드 + 메시지)를 출력
    - `urllib.error.URLError`: URL 관련 오류(네트워크 문제 등)를 출력
    - `PermissionError`: 파일 쓰기 권한 문제를 출력
    - `OSError`: 파일 시스템 관련 일반 오류를 출력
    - 기타 예외는 유형과 상세 정보를 출력

###  `main()`
- 표준 입력에서 첫 줄을 읽어 비디오 수 `N`을 파싱합니다.
- 이후 `N`개의 URL과 이름 쌍을 읽어 리스트에 추가합니다. 입력 형식 오류(빈 URL/이름 등)는 건너뛰고 경고를 출력합니다.
- 유효한 비디오 항목이 하나 이상 있으면 순차적으로 `save_video`를 호출하여 다운로드를 수행합니다.
- 전체 흐름에서 발생할 수 있는 `ValueError`, `EOFError`, `KeyboardInterrupt` 등도 잡아 사용자에게 친절한 메시지를 출력합니다.

###  주의 및 권장 사항

- 파일명에 경로 구분자(`\` 또는 `/`)나 운영체제에서 허용되지 않는 문자를 포함하지 마세요. 현재 코드에는 파일명 검증(정화)이 없습니다.
- 대용량 파일 다운로드 시 디스크 공간과 권한을 확인하세요.
- 병렬 다운로드가 필요하면 현재 코드를 멀티스레드/비동기 방식으로 확장해야 합니다(현재는 순차 다운로드).
- 외부 라이브러리 없이 표준 라이브러리(`urllib`)만 사용하므로 별도 의존성 설치는 필요 없습니다.

###  빠른 수정 팁

- 기본 저장 디렉터리 변경: `save_video` 내부의 `download_path`를 절대 경로로 수정하세요.
- 파일명 충돌 처리 추가: 동일 이름이 존재할 때 덮어쓰지 않도록 `os.path.exists` 검사 후, 번호를 붙이는 등의 로직을 추가하세요.