from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



work = {
    1 : {
    'name':'f1',
    'type': 'old',
    'year': 2017
    }
}

class input(BaseModel):
    name : str
    type : str
    year : int


@app.get('/{id}')
def index(id:int):
    return work[id]



@app.post('/insert/{id}')
def insert_doc(id : int, put : input):
    if id in work:
        return{'error':'available'}
    work[id] = put
    return work[id]

@app.put('/change_data/{id}')
def append_data(id: int, alter : input):
    if id not in work:
        return{'error':'It is not present'}
    if work[id].name != None:
        work[id].name = alter.name
    if work[id].type != None:
        work[id].type = alter.type
    if work[id].year != None:
        work[id].year = alter.year

    return work[id]


@app.delete('/del/{id}')
def delete_id (id : int, cc : input):
    if id not in work:
        return{'error':'It is not present'}
    del work[id]
    return{'message':'deleted'}