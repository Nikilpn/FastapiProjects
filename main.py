from fastapi import FastAPI
app=FastAPI()


@app.get('/')
def Index():
    return "hello world"


@app.get('/dict')
def Indexx():
    return {'data':{'name':'nikhil'}}

def about_page():
    return {"data":"This is my about page"}