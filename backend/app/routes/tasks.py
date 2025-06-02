from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from app.schemas import UserTask
from app.database import AsyncSessionLocal, Task
from fastapi.encoders import jsonable_encoder
from app.utils import get_current_user_id

router = APIRouter(prefix="/tasks", tags=["Создание таск досок"])

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user_task( task_data: UserTask, db: AsyncSession = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    await db.execute(delete(Task).where(Task.user_id == current_user_id, Task.task_id == task_data.task_data[0].task_id))

    new_task = Task(
        user_id=current_user_id,
        task_id= task_data.task_data[0].task_id,
        task_data=jsonable_encoder(task_data.task_data)
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return {"message": "Tasks saved", "task_id": new_task.id}




@router.get("/", status_code=status.HTTP_200_OK)
async def get_user_tasks(
    db: AsyncSession = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id)
):
    result = await db.execute(
        select(Task).where(Task.user_id == current_user_id)
    )
    tasks = result.scalars().all()
    return {"tasks": tasks}
