from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from models import Student, MinData

app = FastAPI()

@app.get('/')
def root():
    return {'message' : 'Root'}


@app.get('/path/{someid}')
def test(someid: int):
    return {
        'id': someid
    }


@app.get('/users')
def getusers(skip: int):
    return {
        'skips' :skip
    }


@app.post('/students')
def getstudents(student: Student):
    return student


@app.post('/usr', response_model=MinData)
def getusr(student: Student):
    return student
    
@app.post('/login')
def login(username: str = Form(), password: str = Form()):
    return {
        'usr': username,
        'pass': password
    }


