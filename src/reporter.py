from analyzer import calculate_risk_level


def shorten_value(value: str, max_length: int = 120) -> str:
    if len(value) <= max_length:
        return value

    return value[:max_length] + "... [truncated]"


def print_report(url: str, results: list[dict]) -> None:
    print("\n========== HTTP Header Security Report ==========\n")
    print(f"Target: {url}\n")

    for result in results:
        header = result["header"]
        status = result["status"].upper()
        value = result["value"]

        symbol = "✓" if result["status"] == "present" else "✗"

        print(f"{symbol} {header}: {status}")

        if value:
            print(f"  Value: {shorten_value(value)}")

        if result["status"] == "missing":
            print(f"  Why it matters : {result['why']}")
            print(f"  Recommendation : {result['recommendation']}")

    present_count = len([r for r in results if r["status"] == "present"])
    missing_count = len([r for r in results if r["status"] == "missing"])

    risk_level = calculate_risk_level(results)

    print("\n========== Summary ==========\n")
    print(f"Headers Present : {present_count}")
    print(f"Headers Missing : {missing_count}")
    print(f"Risk Level      : {risk_level}")
