from fastapi import FastAPI, Request
import uvicorn
import time
import logging
from redis import Redis
from rq import Queue
import mod

logger = logging.getLogger("uvicorn")

app = FastAPI()
q = Queue("main", connection=Redis())


@app.post("/workflow")
async def test(req):
    req_body = await req.json()
    workflow = req_body["product"]

    if hasattr(sys.modules[__name__], workflow):
        print(f"{class_name} exists!")
    else:
        print(f"{class_name} does not exist!")

    q.enqueue(
        f=mod.
    )




job = q.enqueue(
    f=foo,
    # args=(arg1, arg2),
    job_id='foo_123',
    # job_timeout=3600,
    # result_ttl=86400,
    # description='My Job Description',
    # depends_on=my_dependency,
    # at_front=True,
    # meta={'foo': 'bar'}
)
# job = q.enqueue(foo)
job = q.fetch_job('foo_123')
print(job)

time.sleep(2)
print(job.result)
