from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="N5", version="1.0", root_path="/dev/")


@app.get("/MoneoAPIv1")
async def read_root():
    return {"message":"FastAPI running in a lambda function"}


handler = Mangum(app)