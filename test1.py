import importlib
from fastapi import FastAPI, Request
import uvicorn
import os
import time
import logging
from redis import Redis
from rq import Queue
from mod.workflow1 import foo

q = Queue("main", connection=Redis())
# job = q.enqueue(f=foo, job_id='foo_123')
# job1 = q.enqueue(f=foo, job_id='foo_123')

# print(job)
# print(job1)

# time.sleep(2)
# print(job.result)
# print(job1.result)
print(q.fetch_job("foobar"))
print(q.fetch_job("foo_123"))
