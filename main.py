from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/user')

def index(limit=20):
    return {'data':f'{limit}blog list'}


@app.get('/about/{id}')

async def shpw(id:int):
    return {'data': id}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')

def create_blog(request:Blog):
    return {'data':f"blog is created with title as {request.title}"}

'''
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000) 
'''