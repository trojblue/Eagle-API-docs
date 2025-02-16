import os
import requests
import tempfile

from datetime import datetime, timedelta
import threading

from markitdown import MarkItDown

# from .constants import CLEANUP_RATE, TMP_DIR

TMP_DIR = "./tempfiles/"
CLEANUP_RATE = int(60 * 24) # remove files that are 24 hours 


def cleanup_old_files(directory, max_age_minutes):
    """
    Delete files older than max_age_minutes in the background.
    """
    def cleanup_task():
        now = datetime.now()
        threshold = now - timedelta(minutes=max_age_minutes)
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_mod_time = datetime.fromtimestamp(
                    os.path.getmtime(file_path))
                if file_mod_time < threshold:
                    os.remove(file_path)
                    print(f"Deleted old file: {file_path}")

    # Run cleanup in a non-blocking background thread
    threading.Thread(target=cleanup_task, daemon=True).start()


def download_html(url, cleanup=CLEANUP_RATE, tmp_dir=TMP_DIR):
    """
    Download raw HTML from a URL using requests,
    save it to a specified temp directory, and return the file path.
    """
    response = requests.get(url)
    response.raise_for_status()  # Ensure request was successful

    # Ensure the target directory exists
    os.makedirs(tmp_dir, exist_ok=True)

    # Create a temporary file in the specified directory
    fd, temp_file_path = tempfile.mkstemp(suffix=".html", dir=tmp_dir)
    with os.fdopen(fd, 'w', encoding='utf-8') as temp_file:
        temp_file.write(response.text)

    # Trigger cleanup if needed
    if cleanup > 0:
        cleanup_old_files(tmp_dir, cleanup)

    return temp_file_path


def markitdown_to_text(any_input: str):
    """
    Using Markitdown to convert input to markdown.

    Args:
        any_input: filepath or url
    """
    # if not starting with http, check extension
    # if not any_input.startswith("http"):
    #     ext = "." + any_input.split('.')[-1]  # ".ext"
    #     if ext not in MARKITDOWN_SUPPORTED_EXTS:
    #         warnings.warn(
    #             "not in valid exts list; might not be able to convert it")

    md = MarkItDown()
    result = md.convert(any_input)
    return result.text_content


def url_to_md(url: str):
    """
    Convert a URL to markdown.

    Args:
        url: URL to convert to markdown.
    """
    html_file = download_html(url)
    return markitdown_to_text(html_file)