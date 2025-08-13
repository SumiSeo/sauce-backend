from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "coucou,welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createpost")
def create_post(pay_load : dict = Body(...)):
    print(pay_load)
    return {"message": "Successfully created posts",
            "payload":pay_load}

