from fastapi import FastAPI
import uvicorn
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

@app.get("/register")
def say_hello():
    return{"hello":"world"}     

if __name__ =="__main__":
    uvicorn.run("register:app", reload=True)