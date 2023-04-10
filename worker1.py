from rq import Worker, Queue
from redis import Redis

# Create a Redis connection
redis_conn = Redis()

# Create a queue instance
queue = Queue('main', connection=redis_conn)

# Create a worker with a name
worker = Worker(queues=[queue], connection=redis_conn, name='worker1')

# Start the worker
worker.work()
