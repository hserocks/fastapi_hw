from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType

class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root__get():
    return 'string'


@app.post('/post')
def get_post_post_post():
    global post_db
    new_timestamp = Timestamp(id=len(post_db)+1, timestamp=int(round(datetime.datetime.now().hour)))
    post_db.append(new_timestamp)
    return new_timestamp


@app.get('/dog')
def get_dogs_dog_get():
    return dogs_db


@app.post('/dog')
def create_dog_dog_post(dog:Dog):
    global dogs_db
    dogs_db[len(dogs_db) + 1] = dog
    return dog


@app.get('/dog/{pk}')
def get_dog_by_pk_dog__pk__get(pk: int):
    return list(filter(lambda x: x[1].pk == pk, dogs_db.items()))[0][1]


@app.patch('/dog/{pk}')
def update_dog_dog__pk__patch(pk: int, dog:Dog):
    key_num = list(filter(lambda x: x[1].pk == pk, dogs_db.items()))[0][0]
    dogs_db[key_num] =dog
    return dog
