from fastapi import APIRouter
from pydantic

router = APIRouter()




@router.post("/auth/")
async def create_user():
    return {'user' : 'authenticated'}

