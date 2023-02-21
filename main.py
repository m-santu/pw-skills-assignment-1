import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index() :
    return {"page" : "index", "author" : "ankan"}


if __name__ == '__main__' :
    uvicorn.run(app, host='localhost', port=8000)