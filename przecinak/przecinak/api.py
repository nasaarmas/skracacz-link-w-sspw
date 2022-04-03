from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic
from starlette import status

app = FastAPI()


auth = HTTPBasic()

@app.get(f'/')
def index(auth = Depends(auth)):
    print(auth)
    if (auth.username != 'mrokita2'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return 'Hello 5'
