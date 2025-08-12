#!/usr/bin/env python3

import os
import re
import sys
import base64
import argparse
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, unquote

# Default config
DEFAULT_OUTPUT_DIR = 'cloned_site'


def print_banner():
    """Display tool banner and description."""
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                           BURP SUITE XML CLONER                             ║
║                     Extract & Clone Websites from Burp XML                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_usage():
    """Display detailed usage instructions."""
    usage = """
USAGE:
    python3 website-cloner.py <burp_xml_file> [options]

DESCRIPTION:
    This tool parses Burp Suite XML sitemap exports and reconstructs the website
    locally by extracting HTTP responses and organizing them by domain/path.

EXAMPLES:
    # Basic usage - clone to default 'cloned_site' directory
    python3 website-cloner.py burp_sitemap.xml

    # Specify custom output directory
    python3 website-cloner.py burp_sitemap.xml -o /tmp/extracted_site

    # Show help
    python3 website-cloner.py -h

HOW TO EXPORT FROM BURP SUITE:
    1. In Burp Suite, go to Target > Site map
    2. Right-click on the target domain/scope
    3. Select "Save selected items"
    4. Choose "XML format" and save as .xml file
    5. Use that XML file with this tool

OUTPUT STRUCTURE:
    cloned_site/
    ├── example.com/
    │   ├── index.html
    │   ├── login.html
    │   ├── api/
    │   │   └── users.html
    │   └── assets/
    │       ├── style.css
    │       └── script.js
    └── subdomain.example.com/
        └── index.html

SUPPORTED CONTENT:
    ✓ HTML pages
    ✓ CSS stylesheets  
    ✓ JavaScript files
    ✓ JSON API responses
    ✓ Base64 encoded content
    ✓ Binary files (images, etc.)

NOTES:
    • Files are organized by domain and path structure
    • URL parameters and fragments are stripped from filenames
    • Paths ending with '/' get 'index.html' appended
    • Paths without extensions get '.html' appended
    • Invalid filename characters are replaced with underscores
    """
    print(usage)


def sanitize_path(path):
    """Create safe filename from URL path."""
    path = unquote(path)

    # Add index.html for directory paths
    if path.endswith('/'):
        path += 'index.html'

    # Add .html extension if no extension present
    if not os.path.splitext(path)[1]:
        path += '.html'

    # Remove query parameters and fragments
    path = path.split('?')[0].split('#')[0]

    # Replace invalid filename characters
    return re.sub(r'[<>:"\\|?*]', '_', path)


def save_file(domain, path, content, output_dir):
    """Save file to disk with proper directory structure."""
    local_path = sanitize_path(path)
    full_path = os.path.join(output_dir, domain, local_path.lstrip('/'))

    # Create directory structure
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Write file
    with open(full_path, 'wb') as f:
        f.write(content)

    return full_path


def parse_burp_xml(xml_file, output_dir):
    """Parse Burp Suite XML file and extract website content."""
    if not os.path.exists(xml_file):
        print(f"[!] Error: XML file '{xml_file}' not found!")
        return False

    print(f"[+] Parsing Burp XML file: {xml_file}")
    print(f"[+] Output directory: {output_dir}")
    print(f"[+] Creating output directory structure...")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"[!] Error parsing XML file: {e}")
        return False
    except Exception as e:
        print(f"[!] Error reading XML file: {e}")
        return False

    saved_count = 0
    error_count = 0
    domains = set()

    print(f"[+] Processing XML items...")

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
            # Decode content based on encoding
            if is_base64:
                content = base64.b64decode(raw_body)
            else:
                content = raw_body.encode('utf-8')

            # Parse URL components
            parsed = urlparse(url)
            domain = parsed.netloc
            path = parsed.path or '/'

            # Save file
            saved_path = save_file(domain, path, content, output_dir)
            domains.add(domain)
            saved_count += 1

            # Progress indicator
            if saved_count % 10 == 0:
                print(f"[+] Processed {saved_count} files...")

        except Exception as e:
            print(f"[!] Error saving {url}: {e}")
            error_count += 1

    # Summary
    print(f"\n{'=' * 60}")
    print(f"[+] EXTRACTION COMPLETE")
    print(f"[+] Successfully saved: {saved_count} files")
    print(f"[+] Errors encountered: {error_count}")
    print(f"[+] Domains extracted: {len(domains)}")
    print(f"[+] Output location: {os.path.abspath(output_dir)}/")

    if domains:
        print(f"\n[+] Extracted domains:")
        for domain in sorted(domains):
            domain_path = os.path.join(output_dir, domain)
            file_count = sum(len(files) for _, _, files in os.walk(domain_path))
            print(f"    • {domain} ({file_count} files)")

    print(f"{'=' * 60}")
    return True


def main():
    """Main function with argument parsing."""
    parser = argparse.ArgumentParser(
        description='Extract and clone websites from Burp Suite XML exports',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 website-cloner.py burp_sitemap.xml
  python3 website-cloner.py burp_sitemap.xml -o /tmp/extracted_site
  python3 website-cloner.py --help
        """
    )

    parser.add_argument(
        'xml_file',
        help='Burp Suite XML sitemap file to parse'
    )

    parser.add_argument(
        '-o', '--output',
        default=DEFAULT_OUTPUT_DIR,
        help=f'Output directory (default: {DEFAULT_OUTPUT_DIR})'
    )

    parser.add_argument(
        '--usage',
        action='store_true',
        help='Show detailed usage instructions'
    )

    # Handle no arguments
    if len(sys.argv) == 1:
        print_banner()
        parser.print_help()
        print("\nUse --usage for detailed instructions")
        sys.exit(1)

    args = parser.parse_args()

    # Show detailed usage if requested
    if args.usage:
        print_banner()
        print_usage()
        sys.exit(0)

    # Show banner
    print_banner()

    # Parse XML and extract content
    success = parse_burp_xml(args.xml_file, args.output)

    if success:
        print(f"\n[+] Website cloning completed successfully!")
        print(f"[+] Open {os.path.abspath(args.output)}/ to browse extracted content")
    else:
        print(f"\n[!] Website cloning failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()