from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is a list of posts"}