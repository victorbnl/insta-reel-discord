import re
import glob

from yt_dlp import YoutubeDL

from reel_preview.regexes import regexes


def check_url(message_content):
    """Check if message content is a URL. If so, return video url and id."""

    for regex in regexes:
        matches = re.search(regex, message_content)

        if matches:
            state = bool(matches)
            url = matches[0]
            id = matches[1]
            return state, url, id

    return False, None, None


def download(url, filename):
    """Download video and return path."""

    opts = {
        'outtmpl': f'reel/{filename}.%(ext)s',
        'cookiefile': 'cookies.txt',
        'quiet': True,
        'format': '[vcodec=h264]'
    }

    with YoutubeDL(opts) as ytdl:
        ytdl.download([url])

    # Get filename (extension is unknown)
    path = glob.glob(f'reel/{filename}.*')[0]

    return path
