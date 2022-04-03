from fastapi import FastAPI

app = FastAPI()


@app.get(f'/')
def index():
    return 'Hello'
