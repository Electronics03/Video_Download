import urllib.request
import sys
import os
import traceback

read = sys.stdin.readline


def download_progress(block_count, block_size, total_size):
    """Display download progress"""
    downloaded = block_count * block_size
    if total_size > 0:
        percent = min(100, (downloaded / total_size) * 100)
        downloaded_mb = downloaded / (1024 * 1024)
        total_mb = total_size / (1024 * 1024)
        print(
            f"\rProgress: {percent:.1f}% ({downloaded_mb:.2f}MB / {total_mb:.2f}MB)",
            end="",
        )
    else:
        downloaded_mb = downloaded / (1024 * 1024)
        print(f"\rDownloaded: {downloaded_mb:.2f}MB", end="")


def save_video(video_url, save_name):
    """Download video from URL and save to local directory"""
    try:
        download_path = (
            #   "C:\\Users\\...Your local directory address\\"
            +save_name
            + ".mp4"
        )

        directory = os.path.dirname(download_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

        print(f"\nDownloading [{save_name}]...")
        urllib.request.urlretrieve(video_url, download_path, download_progress)
        print(f"\n[{save_name}] is stored in [{download_path}]")

    except urllib.error.HTTPError as e:
        print(f"\nHTTP Error for [{save_name}]: {e.code} - {e.reason}")
        print(f"URL: {video_url}")
    except urllib.error.URLError as e:
        print(f"\nURL Error for [{save_name}]: {e.reason}")
        print(f"URL: {video_url}")
    except PermissionError as e:
        print(f"\nPermission Error for [{save_name}]: Cannot write to {download_path}")
        print(f"Error details: {e}")
    except OSError as e:
        print(f"\nOS Error for [{save_name}]: {e}")
        print(f"Failed to save file to {download_path}")
    except Exception as e:
        print(f"\nUnexpected error occurred while downloading [{save_name}]")
        print(f"Error type: {type(e).__name__}")
        print(f"Error details: {e}")


def main():
    """Main function to handle video downloads"""
    try:
        N = int(read())

        if N <= 0:
            raise ValueError("Number of videos must be greater than 0")

        videos = []

        for i in range(N):
            try:
                url = read().strip()
                video_name = read().rstrip()

                if not url:
                    raise ValueError(f"Empty URL for video {i+1}")
                if not video_name:
                    raise ValueError(f"Empty video name for video {i+1}")

                videos.append((url, video_name))
            except ValueError as e:
                print(f"Input Error for video {i+1}: {e}")
                continue

        if not videos:
            print("No valid videos to download")
        else:
            print(f"\nStarting download of {len(videos)} video(s)...\n")
            for idx, video in enumerate(videos, 1):
                print(f"\n[Video {idx}/{len(videos)}]")
                save_video(video[0], video[1])
            print("\n\nAll downloads completed!")

    except ValueError as e:
        print(f"Value Error: Invalid input format - {e}")
        print(
            "Expected format: First line should be a positive integer (number of videos)"
        )
        print("Then for each video: URL line followed by video name line")
    except EOFError:
        print("EOF Error: Unexpected end of input")
        print("Make sure you provide the correct number of URL and name pairs")
    except KeyboardInterrupt:
        print("\n\nDownload interrupted by user (Ctrl+C)")
    except Exception as e:
        print(f"Unexpected Error: {type(e).__name__}")
        print(f"Error details: {e}")
        print("\nFull traceback:")
        traceback.print_exc()


if __name__ == "__main__":
    main()
