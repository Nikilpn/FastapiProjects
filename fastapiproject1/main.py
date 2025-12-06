from fastapi import FastAPI
app=FastAPI()


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
