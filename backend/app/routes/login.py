from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.schemas import UserLogin
from app.database import AsyncSessionLocal, User
from app.utils import verify_password, create_access_token

router = APIRouter(prefix='/auth', tags=['Логин пользователя'])

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post('/login')
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_data.user_email))

    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    if not verify_password(user_data.user_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid password")
    token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}
