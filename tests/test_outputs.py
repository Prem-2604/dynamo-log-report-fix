import json
from pathlib import Path

REPORT_PATH = Path("/app/perplexity_scores.json")


def _load_report():
    assert REPORT_PATH.exists(), "no perplexity_scores.json found at /app/perplexity_scores.json"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_perplexity_scores():
    report = _load_report()
    expected = {
        "seq_a": 4.780921031756429,
        "seq_b": 4.547752761622072,
        "seq_c": 5.336582012318803,
        "seq_d": 4.828739089166271,
    }
    assert report == expected, f"expected {expected}, got {report}"
