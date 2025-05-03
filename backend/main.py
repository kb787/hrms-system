from fastapi import FastAPI
import uvicorn
from routes.auth_routes import auth_router
from routes.employee_routes import employee_router
from routes.manager_routes import manager_router

app = FastAPI()
app.include_router(auth_router, prefix="/auths", tags=["auth"])
app.include_router(employee_router, prefix="/employee", tags=["employee"])
app.include_router(manager_router,prefix="/manager",tags=["manager"])


@app.get("/")
def home():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081)
