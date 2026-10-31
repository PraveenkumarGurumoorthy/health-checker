from flask import Flask
import redis
import os

app = Flask(__name__)

# Read configuration from environment variables (with fallbacks)
redis_host = os.getenv('REDIS_HOST', 'cache')
redis_port = int(os.getenv('REDIS_PORT', 6379))

cache = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
    except redis.ConnectionError:
        count = "cannot connect to Redis"

    return f"🔥 .env Config Works! This page has been viewed {count} times"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, extra_files=['app.py'])