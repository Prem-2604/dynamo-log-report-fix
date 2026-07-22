import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_is_valid_json():
    """Verifies instruction.md criterion 1: /app/report.json exists and contains valid JSON."""
    report = _load_report()
    assert isinstance(report, dict)


def test_total_requests():
    """Verifies instruction.md criterion 2: total_requests equals the number of lines in the log."""
    report = _load_report()
    assert report.get("total_requests") == 6, f"expected total_requests=6, got {report.get('total_requests')}"


def test_unique_ips():
    """Verifies instruction.md criterion 3: unique_ips equals the number of distinct client IPs in the log."""
    report = _load_report()
    assert report.get("unique_ips") == 3, f"expected unique_ips=3, got {report.get('unique_ips')}"


def test_top_path():
    """Verifies instruction.md criterion 4: top_path equals the most frequently requested path."""
    report = _load_report()
    assert report.get("top_path") == "/index.html", f"expected top_path='/index.html', got {report.get('top_path')}"
