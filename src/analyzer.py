SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]


HEADER_DETAILS = {
    "Strict-Transport-Security": {
        "why": "Forces browsers to use HTTPS for future visits.",
        "recommendation": "Enable HSTS with a strong max-age value.",
    },
    "Content-Security-Policy": {
        "why": "Helps reduce the impact of Cross-Site Scripting attacks.",
        "recommendation": "Configure a Content-Security-Policy for allowed sources.",
    },
    "X-Frame-Options": {
        "why": "Helps prevent clickjacking attacks.",
        "recommendation": "Use DENY or SAMEORIGIN.",
    },
    "X-Content-Type-Options": {
        "why": "Prevents browsers from guessing content types.",
        "recommendation": "Set it to nosniff.",
    },
    "Referrer-Policy": {
        "why": "Controls how much referrer information is shared.",
        "recommendation": "Use a strict Referrer-Policy such as strict-origin-when-cross-origin.",
    },
    "Permissions-Policy": {
        "why": "Restricts browser features like camera, microphone, and geolocation.",
        "recommendation": "Disable unnecessary browser features.",
    },
}
HEADER_DETAILS = {
    "Strict-Transport-Security": {
        "why": "Forces browsers to use HTTPS for future visits.",
        "recommendation": "Enable HSTS with a strong max-age value.",
    },
    "Content-Security-Policy": {
        "why": "Helps reduce the impact of Cross-Site Scripting attacks.",
        "recommendation": "Configure a Content-Security-Policy for allowed sources.",
    },
    "X-Frame-Options": {
        "why": "Helps prevent clickjacking attacks.",
        "recommendation": "Use DENY or SAMEORIGIN.",
    },
    "X-Content-Type-Options": {
        "why": "Prevents browsers from guessing content types.",
        "recommendation": "Set it to nosniff.",
    },
    "Referrer-Policy": {
        "why": "Controls how much referrer information is shared.",
        "recommendation": "Use a strict Referrer-Policy such as strict-origin-when-cross-origin.",
    },
    "Permissions-Policy": {
        "why": "Restricts browser features like camera, microphone, and geolocation.",
        "recommendation": "Disable unnecessary browser features.",
    },
}


def analyze_headers(headers: dict) -> list[dict]:
    results = []

    for header in SECURITY_HEADERS:
        status = "present" if header in headers else "missing"

        results.append({
            "header": header,
            "status": status,
            "value": headers.get(header, ""),
	    "why": HEADER_DETAILS[header]["why"],
   	    "recommendation": HEADER_DETAILS[header]["recommendation"],
        })

    return results

def calculate_risk_level(results: list[dict]) -> str:
    missing_count = len([r for r in results if r["status"] == "missing"])

    if missing_count <= 1:
        return "Low"

    if missing_count <= 3:
        return "Medium"

    return "High"
