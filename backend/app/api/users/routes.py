from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_users():
    return {"message": "List of all users"}

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"User details for user_id {user_id}"}
