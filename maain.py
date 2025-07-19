from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/about")
def about_me():
    return {
        "name": "Miraji Semwanza",
        "profession": "Computer Engineering Student / Software Developer",
        "focus": "Working on FastAPI project for web development",
        "location": "Tanzania",
        "goal": "Learning to build scalable backend APIs with Python FastAPI"
    }

#our databse
items ={
    "1": "cars",
    "2": "banana",
    "3": "apple"
}
@app.get("/items/")
def get_items(page:int=None,per_page: int = None):
    return items


@app.get("/items/{items_id}")
def get_item(item_id:str):
    try:
        item=items[item_id]
        return item
    except KeyError:
        raise HTTPException(status_code=404,detail="items not found")
    
@app.post("/items")
def create_item(item:dict):
    try:
        for k,v in item.items():
            items[k]=v
        return "created successfully"
    except Exception:
        raise HTTPException(status_code=400,detail="invalid data found")



# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: str, item: dict):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if item_id not in item:
        raise HTTPException(status_code=400, detail="ID mismatch in request body")
    
    items[item_id] = item[item_id]
    return {"message": "Item updated successfully", item_id: item[item_id]}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_value = items.pop(item_id)
    return {"message": "Item deleted successfully", "deleted": {item_id: deleted_value}}