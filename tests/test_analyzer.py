import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from analyzer import analyze_headers, calculate_risk_level


def test_analyze_present_header():
    headers = {
        "Strict-Transport-Security": "max-age=31536000"
    }

    results = analyze_headers(headers)

    hsts = results[0]

    assert hsts["header"] == "Strict-Transport-Security"
    assert hsts["status"] == "present"
    assert hsts["value"] == "max-age=31536000"


def test_analyze_missing_header():
    headers = {}

    results = analyze_headers(headers)

    assert results[0]["status"] == "missing"
    assert results[0]["value"] == ""


def test_low_risk_level():
    results = [
        {"status": "present"},
        {"status": "present"},
        {"status": "present"},
        {"status": "present"},
        {"status": "present"},
        {"status": "missing"},
    ]

    assert calculate_risk_level(results) == "Low"


def test_high_risk_level():
    results = [
        {"status": "missing"},
        {"status": "missing"},
        {"status": "missing"},
        {"status": "missing"},
    ]

    assert calculate_risk_level(results) == "High"
