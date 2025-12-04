from fastapi import FastAPI
from pydantic import BaseModel
import cohere
import os
from dotenv import load_dotenv # This is to import the .env file
from phi.agent import Agent
from phi.model.cohere import CohereChat
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv() # This is to load the .env file

class chatRequest(BaseModel): # Creating a class for what the user needs to provide
    prompt: str

class chatResponse(BaseModel): # Creating a class for an output, defines what the server needs to respond
    response: str
    
app = FastAPI() # Creating a FastAPI instance
co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))
agent = Agent(
model=CohereChat(id="command-r-08-2024"),
    show_tool_calls=True,
    markdown=True,
)

@app.get("/") # This is an endpoint, an endpoint is a route that the user can access to get a response
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: chatRequest): # This is a function that will be called when the user sends a request to the 
    response = co.chat(
    model="command-a-03-2025", 
    messages=[{
        "role": "user", 
        "content": request.prompt}]
    )
    
    answer = response.message.content[0].text
    
    print(answer)
    return chatResponse(response=answer)