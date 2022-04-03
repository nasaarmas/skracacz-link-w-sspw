from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic
from starlette import status
from .people import Person

app = FastAPI()


auth = HTTPBasic()

@app.get(f'/')
def index(auth = Depends(auth)):
    print(auth)
    #users is list filled with our users credentials
    users = [Person("imie1", "password1"), 
             Person("imie2", "password2"), 
             Person("imie3", "password3")]

    if not Person(auth.username, auth.password) in users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return 'Hello 5'
