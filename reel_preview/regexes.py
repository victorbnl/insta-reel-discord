import re


regexes = [
    'https:\/\/www\.instagram\.com\/reel\/([a-zA-Z0-9_\-]*)',
    'https:\/\/www\.tiktok\.com\/@[A-z]*\/video\/([a-zA-Z0-9_\-]*)',
]


regexes = [re.compile(s) for s in regexes]
