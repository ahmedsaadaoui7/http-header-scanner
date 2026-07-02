import sys

from fetcher import fetch_headers
from analyzer import analyze_headers
from reporter import print_report
from report_generator import generate_markdown_report
from json_exporter import export_json


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 src/main.py <url>")
        print("Example: python3 src/main.py https://example.com")
        return

    url = sys.argv[1]

    headers = fetch_headers(url)

    if not headers:
    	print(f"Error: Could not fetch headers from '{url}'.")
    	print("Check the URL and try again.")
    	return
    results = analyze_headers(headers)

    print_report(url, results)
    generate_markdown_report(url, results)
    export_json(url, results)


if __name__ == "__main__":
    main()
