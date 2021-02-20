from multiprocessing import cpu_count

bind = '0.0.0.0:8000'
worker_class = 'sync'
workers = cpu_count() * 2 + 1
max_requests = 2048
capture_output = True
