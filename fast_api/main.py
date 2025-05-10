from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello world"}

@app.get("/posts")
def get_posts():
    return {"data": "This is a list of posts"}



# @app.post("/createpost")
# def create_post(payload: dict = Body(...)):
#     return {"message": "Post created successfully", "data": payload}