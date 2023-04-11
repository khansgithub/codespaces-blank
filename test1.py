import importlib
from fastapi import FastAPI, Request
import uvicorn
import os
import time
import logging
from redis import Redis
from rq import Queue, Worker, Connection
from mod.workflow1 import foo

r_con = Redis()
q = Queue("main", connection=r_con)
rq_con = Connection(r_con)
workers = Worker.all(rq_con, queue=q)
for w in workers:
    import ipdb; ipdb.set_trace()
    print(w)