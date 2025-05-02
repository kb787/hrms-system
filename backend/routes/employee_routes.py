from fastapi import APIRouter, Depends
from dependencies.employee import (
    get_all_employee,
    delete_employee,
    create_new_employee,
    update_employee_data,
    get_single_employee,
)
from models.employee_model import EmployeeCreate
from sqlalchemy.orm import Session
from dependencies.manager import get_db

employee_router = APIRouter()


@employee_router.get("/get-all-employee")
def get_all_employee_data(db: Session = Depends(get_db)):
    return get_all_employee(db)


@employee_router.get("/get-single-employee/{empId}")
def get_single_employee_data(empId: int, db: Session = Depends(get_db)):
    return get_single_employee(db, empId)


@employee_router.delete("/delete-employee/{empId}")
def delete_employee_data(empId: int,db: Session = Depends(get_db)):
    return delete_employee(db, empId)


@employee_router.post("/create-employee")
def create_employee_data(employee: EmployeeCreate,db: Session = Depends(get_db)):
    return create_new_employee(db, employee)


@employee_router.patch("/update-employee/{empId}")
def update_employee_data(empId: int, employee: EmployeeCreate,db: Session = Depends(get_db)):
    return update_employee_data(db, empId, employee)
