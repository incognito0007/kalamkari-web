from fastapi import APIRouter

router = APIRouter()

@router.post("/pay")
async def make_payment():
    return {"message": "Process payment"}

@router.get("/history/{user_id}")
async def payment_history(user_id: int):
    return {"message": f"Payment history for user_id {user_id}"}
