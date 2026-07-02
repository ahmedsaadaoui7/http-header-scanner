# HTTP Header Security Scanner

A Python security tool that analyzes HTTP response headers and checks for missing security headers.

This project was built as part of my cybersecurity learning roadmap to understand how web security headers help protect websites against common attacks such as clickjacking, XSS impact, MIME sniffing, information leakage, and insecure transport behavior.

---

## Features

- Fetch HTTP response headers
- Check six important security headers
- Detect present and missing headers
- Explain why each missing header matters
- Provide security recommendations
- Calculate risk level: Low, Medium, High
- Clean terminal report
- Markdown report generation
- JSON report generation
- Unit tests with pytest
- Clean modular architecture

---

## Security Headers Checked

| Header | Purpose |
|--------|---------|
| Strict-Transport-Security | Forces browsers to use HTTPS for future visits |
| Content-Security-Policy | Helps reduce the impact of XSS attacks |
| X-Frame-Options | Helps prevent clickjacking |
| X-Content-Type-Options | Prevents MIME type sniffing |
| Referrer-Policy | Controls referrer information leakage |
| Permissions-Policy | Restricts browser features like camera, microphone, and geolocation |

---

## Technologies Used

- Python 3
- Requests
- JSON
- Markdown
- Pytest
- Git

---

## Project Structure

```text
http-header-scanner/
│
├── src/
│   ├── main.py
│   ├── fetcher.py
│   ├── analyzer.py
│   ├── reporter.py
│   ├── report_generator.py
│   └── json_exporter.py
│
├── tests/
│   └── test_analyzer.py
│
├── reports/
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/http-header-scanner.git
cd http-header-scanner
pip install -r requirements.txt
```

---

## Usage

```bash
python3 src/main.py https://example.com
```

Example:

```bash
python3 src/main.py https://github.com
```

---

## Example Output

```text
========== HTTP Header Security Report ==========

Target: https://github.com

✓ Strict-Transport-Security: PRESENT
  Value: max-age=31536000; includeSubdomains; preload

✓ Content-Security-Policy: PRESENT
  Value: default-src 'none'; base-uri 'self'; child-src... [truncated]

✗ Permissions-Policy: MISSING
  Why it matters : Restricts browser features like camera, microphone, and geolocation.
  Recommendation : Disable unnecessary browser features.

========== Summary ==========

Headers Present : 5
Headers Missing : 1
Risk Level      : Low
```

---

## Reports

The tool generates:

```text
reports/header_security_report.md
reports/header_security_report.json
```

---

## Run Tests

```bash
pytest
```

---

## Future Improvements

- Add more security headers
- Add CSV export
- Add severity score per header
- Add colored terminal output
- Add batch scanning for multiple URLs
- Add better URL normalization
- Add HTML report generation

---

## Author

Ahmed Saadaoui

Cybersecurity Student
Python Automation
Future SOC Analyst / Penetration Tester
