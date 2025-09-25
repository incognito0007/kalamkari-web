from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_contents():
    return {"message": "List of all content"}

@router.post("/")
async def create_content():
    return {"message": "Create new content"}

@router.get("/{content_id}")
async def get_content(content_id: int):
    return {"message": f"Details for content_id {content_id}"}
