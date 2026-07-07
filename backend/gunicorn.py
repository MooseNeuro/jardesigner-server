bind = "0.0.0.0:5000"
worker_class = "geventwebsocket.gunicorn.workers.GeventWebSocketWorker"
workers = 1                  # SocketIO requires 1 worker (scale with Redis later)
timeout = 0           # 0 disables the worker timeout so long-running sessions aren't killed
loglevel = "info"
errorlog = "/app/logs/error.log"
accesslog = "/app/logs/access.log"
