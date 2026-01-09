from fastapi import FastAPI
app=FastAPI()
from pydantic import BaseModel
from typing import Optional
import uvicorn

@app.get('/')
def Index():
    return {'data':'blog list'}


@app.get('/blog/unpublished')
def unpublished():
    return {}


@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments():
    return {'data'}





@app.get('/about')
def about_page():
    return {"data":"This is my about pages"}

@app.get('about/same')
def about_page():
    return {"data":"this iis also my about Page"}




class Blog(BaseModel):
    title:str
    description:str
    published:Optional[bool]

@app.post('/blog')
def blog_create(request:Blog):
    return request
    return {'data':'blog created'}



# if __name__=="__main__":
#     uvicorn.run(app,host='127.0.0.1',port=9000)
