from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Step 1: Create the model
class Item(BaseModel):
    id: str
    name: str

# Step 2: Fake database
items = {
    "1": "cars",
    "2": "banana",
    "3": "apple"
}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.post("/items")
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.id] = item.name
    return {"message": "Item created", item.id: item.name}

@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    if item_id != item.id:
        raise HTTPException(status_code=400, detail="ID mismatch")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item.id] = item.name
    return {"message": "Item updated", item.id: item.name}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = items.pop(item_id)
    return {"message": "Item deleted", "deleted": {item_id: deleted}}
