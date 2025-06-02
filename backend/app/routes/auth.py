from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.schemas import UserRegister
from app.database import AsyncSessionLocal, User
from app.utils import hash_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Регистрация пользователей"])

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/register")
async def register(user_create: UserRegister, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_create.user_email))
    user = result.scalars().first()
    if user:
        raise HTTPException(status_code=400,detail="Email is registered")
    hashed_pwd = hash_password(user_create.user_password)
    new_user = User(email=user_create.user_email,hashed_password=hashed_pwd, create_at=user_create.user_create_at)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    token = create_access_token(data={"sub": str(new_user.id)})
    return {"access_token": token, "token_type":"bearer"}