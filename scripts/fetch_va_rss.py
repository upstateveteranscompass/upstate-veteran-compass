#!/usr/bin/env python3
"""Fetch the official VA news-release RSS feed and write JSON for the website."""
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path

FEED_URL = "https://news.va.gov/news-releases/feed/"
OUTPUT = Path("news.json")
MAX_ITEMS = 30

def clean_text(value):
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", unescape(value)).strip()

def iso_date(value):
    if not value:
        return ""
    try:
        return parsedate_to_datetime(value).isoformat()
    except (TypeError, ValueError, OverflowError):
        return value

def main():
    request = urllib.request.Request(FEED_URL, headers={"User-Agent": "UpstateVeteranCompass/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        xml_data = response.read()
    root = ET.fromstring(xml_data)
    items = []
    for item in root.findall(".//item")[:MAX_ITEMS]:
        title = clean_text(item.findtext("title", default=""))
        link = (item.findtext("link", default="") or "").strip()
        summary = clean_text(item.findtext("description", default=""))
        pub_date = iso_date(item.findtext("pubDate", default=""))
        if not title or not link.startswith("https://news.va.gov/"):
            continue
        items.append({"title": title[:300], "link": link, "date": pub_date,
                      "summary": summary[:420], "source": "U.S. Department of Veterans Affairs"})
    if not items:
        raise RuntimeError("No usable items found in feed; no output written.")
    OUTPUT.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} VA news items to {OUTPUT}")

if __name__ == "__main__":
    main()
