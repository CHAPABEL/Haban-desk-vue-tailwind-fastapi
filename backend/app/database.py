from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, BigInteger

DATABASE_URL="postgresql+asyncpg://myuser:mypassword@postgres:5432/mydatabase"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal= sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password= Column(String, nullable=False)
    create_at = Column(String, nullable=False)

    tasks = relationship('Task', back_populates="user", cascade='all,delete')


class Task(Base):
    __tablename__="tasks"

    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey(User.id))
    task_id=Column(BigInteger)
    task_data= Column(JSON)
    user = relationship('User', back_populates='tasks')