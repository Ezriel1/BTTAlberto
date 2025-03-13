from fastapi import FastAPI

app = FastAPI() #constructor that keeps API open to wait for someone to access it

@app.get("/") # endpoint to access the FastAPI using the GET method, () indicate that it's a function
def root():
    return "Hello world"

