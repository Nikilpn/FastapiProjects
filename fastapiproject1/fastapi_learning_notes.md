fastapi 
---------------------
superfast python webframework

features
=====
automatic documentation (swagger ui,redoc)
fast
security
starlette features-eg-websocket 
_____________


----install fastapi----
pip3 install fastapi

----uvicorn--
pip3 install uvicorn


----uvicorn--runserver---------------------------------------------------------

run in port 8000 default
------------------

uvicorn main:app --reload

run in another port 9000
uvicorn blog.main:app --reload --port 9000

run another python file which is located in another folder for example there is a blog folder and we have a main file in there for running it 

uvicorn blog.main:app --reload

--------------------------
run in another port 9000

if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=9000)


run--->python3 main.py
---------------------------------------------------------------------------------


________________________

pydantic library
-all the validations are done by pydantic library

_______________
swagger ui-

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc


-__________________
debug fastapi
_________________
ctrl+shift+p---select debug
add breakpoint
run swagger apply varialble in data
choose debug in  vs code
---------------------


__________connecting to database______________________
first step:make schemas.py
make models.py
and connect it 

step2:fastapi need sqlAlchemy

    pip install SQLAlchemy

make database.py