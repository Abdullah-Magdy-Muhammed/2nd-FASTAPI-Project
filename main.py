from fastapi import FastAPI


app = FastAPI()

@app.get('/user')

def index():
    return {'data':{'name': 'abdullah'}}


@app.get('/about')

def about():
    return {'data': 'about our app'}
