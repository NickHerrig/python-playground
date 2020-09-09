from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram, Info, Enum, ProcessCollector
import random
import time

"""
Metric Examples:

Counter - A cumulative metric whose value can only increase or be reset on restart.
Gauge - A metric that reperesents a single numerical value that can arbitrarily go up and down.
Histogram - Counts metrics and places them in configurable buckets, also provides sums(request duration and sizes).
Summary - Similar to histogram, but over a sliding time window.

"""

c = Counter('total_failures', 'Number of failures due to network errors')
g = Gauge('in_process_requests', 'Number of failures due to network errors')
i = Info('my_app_info', 'The application version info')
e = Enum('my_app_state', 'The current state of the application',  states=['started', 'stopped'])
p = ProcessCollector(namespace='mydaemon', pid=lambda: open('/var/run/daemon.pid').read())

if __name__ == '__main__':
    start_http_server(8001)
    while True:
        pass

