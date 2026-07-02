from datetime import datetime
from analyzer import calculate_risk_level


def shorten_value(value: str, max_length: int = 120) -> str:
    if len(value) <= max_length:
        return value

    return value[:max_length] + "... [truncated]"

def generate_markdown_report(url: str, results: list[dict]) -> None:
    filename = "reports/header_security_report.md"

    present_count = len([r for r in results if r["status"] == "present"])
    missing_count = len([r for r in results if r["status"] == "missing"])
    risk_level = calculate_risk_level(results)

    with open(filename, "w") as report:
        report.write("# HTTP Header Security Report\n\n")
        report.write(f"**Target:** {url}\n\n")
        report.write(f"**Scan Date:** {datetime.now()}\n\n")

        report.write("| Header | Status | Value | Why it matters | Recommendation |\n")
        report.write("|--------|--------|-------|----------------|----------------|\n")

        for result in results:
            value = shorten_value(result["value"]) if result["value"] else "-"
            report.write(
                f"| {result['header']} | "
                f"{result['status'].upper()} | "
                f"{value} | "
                f"{result['why']} | "
                f"{result['recommendation']} |\n"
            )

        report.write("\n## Summary\n\n")
        report.write(f"- Headers Present: {present_count}\n")
        report.write(f"- Headers Missing: {missing_count}\n")
        report.write(f"- Risk Level: {risk_level}\n")

    print(f"\nMarkdown report saved to: {filename}")
