from fastapi import FastAPI
import uvicorn
from routes.auth_routes import auth_router
from routes.employee_routes import employee_router

app = FastAPI()
app.include_router(auth_router, prefix="/auths", tags=["auth"])
app.include_router(employee_router, prefix="/employee", tags=["employee"])


@app.get("/")
def home():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081)
