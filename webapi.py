from fastapi import FastAPI
from pydantic import BaseModel
from rq import Queue
from worker import conn
from util import do_some_work

class QueueRequest(BaseModel):
    text: str

app = FastAPI()

q = Queue(connection=conn)

@app.post("/queue/")
async def create_createRequest(queueRequest: QueueRequest):

    result = q.enqueue(do_some_work, queueRequest.text)

    return "ok"
