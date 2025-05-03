from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from models.manager_model import ManagerCreate
from dependencies.manager import (
    get_db,
    get_all_managers,
    get_single_manager,
    approve_employee_leave,
    reject_employee_leave,
    find_all_employees_associated,
    find_faulty_employees,
    give_pay_hike,
    give_pay_cut,
    create_new_manager,
    delete_manager,
    update_manager_details
    
)

manager_router = APIRouter()

@manager_router.get("/get-manager-list")
def get_manager_list(db : Session = Depends(get_db)):
    return get_all_managers(db)

@manager_router.get("/get-manager-data/{manId}")
def get_manager_data(manId : int , db : Session = Depends(get_db)):
     return get_single_manager(manId,db)
 
@manager_router.get("/get-all-employees-associated/{manId}")
def get_all_employee_data(manId:int , db: Session = Depends(get_db)):
     return find_all_employees_associated(manId,db)
    
@manager_router.get("/get-faulty-employees/{manId}") 
def get_faulty_employees(manId:int , db: Session = Depends(get_db)):
    return find_faulty_employees(manId,db)

@manager_router.patch("/approve-employee-leave/{empId}")
def approve_employee_leave(empId:int , db: Session = Depends(get_db)):
    return approve_employee_leave(empId,db) 

@manager_router.patch("/reject-employee-leave/{empId}")
def reject_employee_leave(empId:int , db: Session = Depends(get_db)):
    return reject_employee_leave(empId,db) 

@manager_router.patch("/give-pay-hike/{manId}/{empId}")
def give_employee_hike(manId:int, empId:int , db: Session = Depends(get_db)):
    return give_pay_hike(manId,empId,db)

@manager_router.patch("/give-pay-cut/{manId}/{empId}")
def give_employee_cut(manId:int , empId:int, db: Session = Depends(get_db)):
    return give_pay_cut(manId,empId,db) 

@manager_router.post("/create-new-manager")
def create_manager(manager:ManagerCreate,db: Session = Depends(get_db)):
    return create_new_manager(db,manager)
    
@manager_router.delete("/delete-manager/{manId}")
def delete_manager(manId: int , db : Session = Depends(get_db)):
    return delete_manager(manId,db)    

@manager_router.patch("/update-manager/{manId}")
def update_manager(manId : int , manager: ManagerCreate, db:Session = Depends(get_db)):
    return update_manager_details(manId,manager,db)