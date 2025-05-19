from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:5173",
     "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserRegister(BaseModel):
    user_email: str
    user_password: str

@app.post("/register")
def register(user: UserRegister):
    return {"message": f"userEmail: {user.user_email} Reg"}

@app.get("/register")
def print_register():
    return {"message": "Register working"}

if __name__ =="__main__":
    import uvicorn
    uvicorn.run("register:app", reload=True)