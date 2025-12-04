from fastapi import FastAPI
from pydantic import BaseModel
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

class chatRequest(BaseModel): # Creating a class for what the user needs to provide
    prompt: str

class chatResponse(BaseModel): # Creating a class for an output, defines what the server needs to respond
    response: str
    
app = FastAPI() # Creating a FastAPI instance
co = cohere.ClientV2(api_key="COHERE_API_KEY")

@app.get("/") # This is an endpoint, an endpoint is a route that the user can access to get a response
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: chatRequest): # This is a function that will be called when the user sends a request to the endpoint
    return chatResponse(response="I will get stinkier later!")