from sqlalchemy.orm import Session
from models.employee_model import Employee
from config.config import SessionLocal, engine, Base
from models.manager_model import Manager
from models.employee_model import Employee
from fastapi import HTTPException, status

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


def get_all_managers(db: Session):
    try:
        manager_obj = db.query(Manager).all()
        if not manager_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Manager not found"
            )
        return (status.HTTP_200_OK, manager_obj)
    except Exception as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server side error occured"
        )


def get_single_manager(manId: int, db: Session):
    try:
        target_manager = db.query(Manager).filter(Manager.manager_id == manId)
        if not target_manager:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Manager not found"
            )
        return (status.HTTP_200_OK, target_manager)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server side error occurred",
        )


def approve_employee_leave(empId: int, db: Session):
    try:
        target_employee = db.query(Employee).filter(Employee.employee_id == empId).all()
        if not target_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
            )
        target_employee.leave_approve_status = True
        db.commit()
        return (status.HTTP_200_OK, {"message": "Leave approved successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server side error occured")


def reject_employee_leave(empId: int, db: Session):
    try:
        target_employee = db.query(Employee).filter(Employee.employee_id == empId)
        if not target_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
            )
        else:
            target_employee.leave_approve_status = False
            db.commit()
            return (status.HTTP_200_OK, {"messsage": "Leave request rejected"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server side error occured")


def find_all_employees_associated(manId: int, db: Session):
    try:
        target_employee = (
            db.query(Manager, Employee)
            .filter(Manager.manager_id == manId)
            .join(Manager, Employee.employee_id == Manager.employee_id)
            .all()
        )
        if not target_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
            )
        return (status.HTTP_200_OK, target_employee)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server side error occured")


def find_faulty_employees(manId: int, db: Session):
    try:
        target_employees = (
            db.query(Manager, Employee)
            .filter(Manager.manager_id == manId)
            .join(Manager, Employee.employee_id == Manager.employee_id)
            .all()
        )
        if not target_employees:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
            )
        faulty_employees = target_employees.filter(
            target_employees.late_remarks > 4
        ).all()
        if not faulty_employees:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No faulty employees found",
            )
        return (status.HTTP_200_OK, target_employees)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server side error occured")


def give_pay_hike(manId: int, empId: int, db: Session):
    try:
        get_all_associated_employee = (
            db.query(Manager, Employee)
            .filter(Manager.manager_id == manId)
            .join(Manager, Employee.employee_id == Manager.employee_id)
            .all()
        )
        if not get_all_associated_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found for corresponding manager",
            )
        target_employee = get_all_associated_employee.filter(
            Employee.employee_id == empId
        )
        if not target_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee with provided id does not exists",
            )
        target_employee.salary = (
            target_employee.salary + target_employee.increment_amount
        )
        db.commit()
        return (status.HTTP_200_OK, {"message": "Pay hike given successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server side error occured")


def give_pay_cut(manId: int, empId: int, db: Session):
    try:
        get_associated_employee = (
            db.query(Manager, Employee)
            .filter(Manager.manager_id == manId)
            .join(Manager, Employee.employee_id == Manager.employee_id)
            .all()
        )
        if not get_associated_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detaiql="No associated employee found for corresponding manager",
            )
        target_employee = get_associated_employee.filter(Employee.employee_id == empId)
        target_employee.salary = (
            target_employee.salary - target_employee.decrement_amount
        )
        db.commit()
        return (status.HTTP_200_OK, {"message": "Pay cut performed successfully"})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occured",
        )


def create_new_manager(manager: Manager,db: Session):
    try:
        new_manager = Manager(
            employee_id=manager.employee_id,
            manager_first_name=manager.manager_first_name,
            manager_last_name=manager.manager_last_name,
            manager_age=manager.manager_age,
            manager_salary=manager.manager_salary,
            manager_late_remarks=0,
            manager_joining_date=manager.manager_joining_date,
            manager_increment_amount=manager.manager_increment_amount,
            manager_decrement_amount=manager.manager_decrement_amount,
            manager_pending_leaves=manager.manager_pending_leaves,
            manager_leave_approve_status=False,
        )
        db.add(new_manager)
        db.commit()
        return (status.HTTP_201_CREATED, {"message": "Manager created successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server side error occured")


def delete_manager(manId: int, db: Session):
    try:
        target_manager = db.query(Manager).filter(Manager.manager_id == manId)
        if not target_manager:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Manager not found"
            )
        target_manager.delete()
        db.commit()
        return (status.HTTP_200_OK, {"message": "Manager deleted successfully"})
    except Exception as e:
        return (
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            {"message": "Server side error occured"},
        )


def update_manager_details(manId: int, manager: Manager, db: Session):
    try:
        target_manager = db.query(Manager).filter(Manager.manager_id == manId)
        if not target_manager:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Manager not found",
            )
        target_manager.update(
            {
                Manager.manager_first_name: manager.manager_first_name,
                Manager.manager_last_name: manager.manager_last_name,
                Manager.manager_age: manager.manager_age,
                Manager.manager_salary: manager.manager_salary,
                Manager.manager_late_remarks: manager.manager_late_remarks,
                Manager.manager_joining_date: manager.manager_joining_date,
                Manager.manager_increment_amount: manager.manager_increment_amount,
                Manager.manager_decrement_amount: manager.manager_decrement_amount,
                Manager.manager_pending_leaves: manager.manager_pending_leaves,
                Manager.manager_leave_approve_status: manager.manager_leave_approve_status,
            }
        )
        db.commit()
        return (status.HTTP_200_OK, {"message": "Manager details successfully updated"})

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occured",
        )
