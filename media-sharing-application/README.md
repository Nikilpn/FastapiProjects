uv init .

uv add fastapi
uv add python-dotenv
uv add fastapi-users[sqlalchemy]

uv add imagekitio

uv add uvicorn[standard]

uv add aiosqlite

folder created -app folder
    1.app.py

    from fastapi import FastAPI

    app=FastAPI()

    @app.get("/hello-world")
    def hello_world():
        return{"message":"hello world"}


2.main.py 
----------
import uvicorn 

if __name__ == "__main__":
    uvicorn.run("app.app:app",host="0.0.0.0",port=8000,reload=True)

3.check its running or not using command 
-----------------------------------
uv run ./main.py

4.can also run in http://localhost:8000/docs

5.
