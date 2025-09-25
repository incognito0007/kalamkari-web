from fastapi import FastAPI
from app.api import auth, users, content, payments

app = FastAPI(title="kalamKari Backend API")

app.include_router(auth.auth_router, prefix="/auth", tags=["auth"])
app.include_router(users.user_router, prefix="/users", tags=["users"])
app.include_router(content.content_router, prefix="/content", tags=["content"])
app.include_router(payments.payment_router, prefix="/payments", tags=["payments"])

@app.get("/")
async def read_root():
    return {"message": "kalamKari backend is running!"}