from fastapi import FastAPI
import uvicorn
from backend.routes.auth_routes import auth_router

app = FastAPI()
app.include_router(auth_router, prefix="/auths", tags=["auth"])


@app.get("/")
def home():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081)
