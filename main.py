import uvicorn
from fastapi import FastAPI
import Script
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, reload=True)

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str
    status: str
    tags: List[str]

class TicketUpdate(BaseModel):
    status: Optional[str] = None

@app.get("/")
def root():
    return ("salut !")

@app.get("/tickets")
def ReadTickets():
    return Script.file()

@app.post("/tickets")
def CreerTickets(item:TicketCreate):
    title = item.title
    description = item.description
    priority = item.priority
    status = item.status    
    tags=item.tags
    return Script.TicketAdd(title,description,priority,status,tags)

@app.patch("/tickets/{id}")
def ModifTickets(id:int ,item: TicketUpdate):
    status=item.status
    return Script.TicketUpdate(id,status)

@app.delete("/tickets/{id}")
def DelTickets(id:int):
    return Script.TicketDelete(id)


