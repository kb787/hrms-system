from sqlalchemy.orm import Session
from backend.models.employee_model import Employee
from backend.config.config import SessionLocal , engine, Base
from backend.models.manager_model import Manager

def get_db():
    db = SessionLocal()
    try:
       yield db
       
    finally:
       db.close()
       
def get_all_managers(db: Session):
    return db.query(Manager,Employee).join(Employee,Employee.employee_id == Manager.employee_id).all() ;             
        
def get_single_manager(db : Session, manId : int):
    return db.query(Manager).filter(Manager.manager_id == manId).join(Employee,Employee.employee_id == Manager.employee_id).all() 