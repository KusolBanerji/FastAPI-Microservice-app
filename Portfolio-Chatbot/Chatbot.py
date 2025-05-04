from fastapi import APIRouter, Depends, Body

router = APIRouter()

@router.post("/portfolio-chatbot")
async def reply(message: str = Body(...),token: str = Body(...)):
    if token != "sent-from-Kusol's-portfolio":
        return {"reply": "Invalid token"}
    return {"reply": "Replied from FastAPI"}