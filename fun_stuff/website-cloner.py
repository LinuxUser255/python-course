#!/usr/bin/env python3

import os
import re
import base64
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, unquote

# Config
BURP_XML_FILE = 'burp_sitemap.xml'
OUTPUT_DIR = 'cloned_site'

# Create safe filename from URL path
def sanitize_path(path):
    path = unquote(path)
    if path.endswith('/'):
        path += 'index.html'
    if not os.path.splitext(path)[1]:
        path += '.html'
    path = path.split('?')[0].split('#')[0]
    return re.sub(r'[<>:"\\|?*]', '_', path)

# Save file to disk
def save_file(domain, path, content):
    local_path = sanitize_path(path)
    full_path = os.path.join(OUTPUT_DIR, domain, local_path.lstrip('/'))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'wb') as f:
        f.write(content)

def parse_burp_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    saved_count = 0

    for item in root.findall('item'):
        url = item.findtext('url')
        response_el = item.find('response')

        if not url or response_el is None:
            continue

        raw_body = response_el.text
        is_base64 = response_el.attrib.get('base64', 'false') == 'true'

        if raw_body is None:
            continue

        try:
            content = base64.b64decode(raw_body) if is_base64 else raw_body.encode('utf-8')
            parsed = urlparse(url)
            domain = parsed.netloc
            path = parsed.path or '/'
            save_file(domain, path, content)
            saved_count += 1
        except Exception as e:
            print(f"[!] Error saving {url}: {e}")

    print(f"[+] Done. Saved {saved_count} files into {OUTPUT_DIR}/")

if __name__ == '__main__':
    parse_burp_xml(BURP_XML_FILE)
