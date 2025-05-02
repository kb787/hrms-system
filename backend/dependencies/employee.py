from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.employee_model import Employee
from config.config import SessionLocal, engine, Base


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


def get_all_employee(db: Session):
    employee_obj = db.query(Employee).first()
    if not employee_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
        )
    return (status.HTTP_200_OK, employee_obj)


def delete_employee(empId: int,db: Session):
    target_employee = db.query(Employee).filter(Employee.employee_id == empId)
    if not target_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
        )
    Session.delete(target_employee)
    Session.commit()
    return (status.HTTP_200_OK, {"message": "Employee deleted successfully"})


def create_new_employee(db: Session, employee: Employee):
    try:
        new_employee = Employee(
            first_name=employee.first_name,
            last_name=employee.last_name,
            age=employee.age,
            designation=employee.designation,
            salary=employee.salary,
            late_remarks=0,
            joining_date=employee.joining_date,
            increment_amount=employee.increment_amount,
            decrement_amount=employee.decrement_amount,
            pending_leaves=employee.pending_leaves,
            leave_approve_status=employee.leave_approve_status(default=False),
        )
        db.add(new_employee)
        db.commit()
        return (status.HTTP_201_CREATED, {"message": "Employee created successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating employee")


def update_employee_data(empId: int,employee: Employee,db: Session):
    try:
        target_employee = db.query(Employee).filter(Employee.employee_id == empId)
        if not target_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
            )  
        target_employee.update(
            {
                Employee.first_name: employee.first_name,
                Employee.last_name: employee.last_name,
                Employee.age: employee.age,
                Employee.designation: employee.designation,
                Employee.salary: employee.salary,
                Employee.late_remarks: employee.late_remarks,
                Employee.joining_date: employee.joining_date,
                Employee.increment_amount: employee.increment_amount,
                Employee.decrement_amount: employee.decrement_amount,
                Employee.pending_leaves: employee.pending_leaves,
                Employee.leave_approve_status: employee.leave_approve_status,
            }
        )
        return (status.HTTP_200_OK, {"message": "Employee updated successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error updating employee")


def get_single_employee(empId: int,db: Session):
    target_employee = db.query(Employee).filter(Employee.employee_id == empId)
    if not target_employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return (status.HTTP_200_OK, target_employee)
