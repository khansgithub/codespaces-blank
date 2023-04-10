import time
from redis import Redis
from rq import Queue
from mod.workflow1 import Main, foo

q = Queue("main", connection=Redis())

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
