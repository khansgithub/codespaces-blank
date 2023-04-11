from contextlib import asynccontextmanager
import importlib
from fastapi import FastAPI, Request
import uvicorn
import os
import time
import logging
from redis import Redis
from rq import Queue
import uuid

@asynccontextmanager
async def lifespan(app: FastAPI):
    import_modules()
    yield

PORT=3000
logger = logging.getLogger("uvicorn")
workflow_modules = {}
q = Queue("main", connection=Redis())
app = FastAPI(lifespan=lifespan)

def import_modules():
    module_root = "mod"
    directory_path = f"./{module_root}/"

    for module in os.listdir(directory_path):
        if not os.path.isdir(os.path.join(directory_path, module)):
            continue
        if module[0] == ".": continue

        module_name = f"{module_root}.{module}"
        spec = importlib.util.find_spec(module_name)
        if spec is None: continue
        improted_module = importlib.import_module(module_name)
        workflow_modules[module] = improted_module


@app.post("/workflow")
async def test(req: Request):
    req_body = await req.json()
    print(req_body)
    workflow = req_body["product"]

    if workflow not in workflow_modules:
        raise Exception("Product does not exist")

    workflow_object = workflow_modules[workflow].Main()
    job_id = req_body["id"]

    if q.fetch_job(job_id) is not None:
        raise Exception(f"Job id {job_id=} already exists")

    print(q.enqueue(
        f=workflow_object.run,
        job_id=job_id
    ))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=PORT,
        reload=True
    )


# job = q.enqueue(
#     f=foo,
#     # args=(arg1, arg2),
#     job_id='foo_123',
#     # job_timeout=3600,
#     # result_ttl=86400,
#     # description='My Job Description',
#     # depends_on=my_dependency,
#     # at_front=True,
#     # meta={'foo': 'bar'}
# )
# # job = q.enqueue(foo)
# job = q.fetch_job('foo_123')
# print(job)

# time.sleep(2)
# print(job.result)
