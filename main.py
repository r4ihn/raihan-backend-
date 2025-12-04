from fastapi import FastAPI

app = FastAPI()

@app.get("/") # This is an endpoint, an endpoint is a route that the user can access to get a response
def health():
    return {"status": "ok"}