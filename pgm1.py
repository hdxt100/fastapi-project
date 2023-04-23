from fastapi import FASTAPI
from pydantic import BaseModel

a = {

    1 : {
    'vehicke' : 'alto',
    'type' : 'car',
    'model' : 2017
    },
     2 : {
     'vehicle' : 'bmw',
     'type' : 'supercar',
     'model' : 2023
    }
 }

app = FASTAPI()

class input(BaseModel):
    vehicle : str
    type : str
    model : int



@app.get('/')
def index():
    return{'hello':'tinu'}


@app.post('/enter_car/{car_id}')
def enter_car(car_id : int, b : input):
    if car_id in a:
        return{'error':'already available'}
    a[car_id] = b
    return a[car_id]

