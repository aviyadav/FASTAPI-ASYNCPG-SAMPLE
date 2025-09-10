from fastapi import FastAPI
from db import Database

app = FastAPI()
db = Database(dsn="postgresql://postgres:password@localhost:5432/pocdb")

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

@app.get("/users")
async def get_users():
    users = await db.fetch_users()
    return {"users": [dict(user) for user in users]}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await db.fetch("SELECT id, name, email FROM users WHERE id = $1", user_id)
    if user:
        return {"user": dict(user[0])}
    return {"error": "User not found"}, 404

@app.post("/users")
async def create_user(name: str, email: str):
    result = await db.execute(
        "INSERT INTO users (name, email) VALUES ($1, $2) RETURNING id", name, email
    )
    return {"result": result}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    result = await db.execute("DELETE FROM users WHERE id = $1", user_id)
    return {"result": result}