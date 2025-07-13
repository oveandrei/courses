from prometheuse_client import start_http_server, Counter

REQUESTS = Counter("http_requests_total", "Total HTTP Requests")
start_http_server(8001) # expose / metrics

