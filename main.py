from fastapi import FastAPI
from db import checkIfTableExist, addItemToList

app = FastAPI()

checkIfTableExist()

@app.get("/")
def seven22():
    return 'seven22'

@app.post("/createliste")
def add(child, id, city, text, gifts):
    return addItemToList(child, id, city, text, gifts)

@app.get('/getitemfromlist')
def get():
    pass