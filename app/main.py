from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .db import people_coll

app = FastAPI(title="People API", version="1.0.0")

class Person(BaseModel):
    id: str
    name: str
    email: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/person")
def list_people():
    return [
        {"id": str(doc.get("_id")), "name": doc.get("name"), "email": doc.get("email")}
        for doc in people_coll.find({}, {"name": 1, "email": 1})
    ]

@app.post("/person/{pid}")
def add_person(pid: str, person: Person):
    if pid != person.id:
        raise HTTPException(status_code=400, detail="Path ID and body ID mismatch")
    people_coll.insert_one({"_id": pid, "name": person.name, "email": person.email})
    return {"inserted": pid}
