import json
from datetime import datetime

from analyzer import calculate_risk_level


def export_json(url: str, results: list[dict]) -> None:
    filename = "reports/header_security_report.json"

    report = {
        "target": url,
        "scan_date": str(datetime.now()),
        "headers_present": len([r for r in results if r["status"] == "present"]),
        "headers_missing": len([r for r in results if r["status"] == "missing"]),
        "risk_level": calculate_risk_level(results),
        "results": results,
    }

    with open(filename, "w") as json_file:
        json.dump(report, json_file, indent=4)

    print(f"JSON report saved to: {filename}")
