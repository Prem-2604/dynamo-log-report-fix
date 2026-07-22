There's an access log at /app/access.log, in Apache combined log format. Parse it and write a JSON summary report to /app/report.json.

The report must be a JSON object with exactly these three keys:
- total_requests: the total number of log lines, as an integer
- unique_ips: the number of distinct client IP addresses, as an integer
- top_path: the request path (e.g. "/index.html") requested most often, as a string

Success criteria:
1. /app/report.json exists and contains valid JSON.
2. total_requests equals the number of lines in the log.
3. unique_ips equals the number of distinct client IPs found in the log.
4. top_path equals whichever request path appears most frequently across all log entries.
