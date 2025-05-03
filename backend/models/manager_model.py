from sqlalchemy import String, Boolean, Integer, BigInteger, Column, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Manager(Base):
    __tablename__ = "managers"
    employee_id = Column(Integer, ForeignKey("employees.employee_id"), nullable=False)
    manager_id = Column(Integer, primary_key=True, index=True)
    manager_first_name = Column(String)
    manager_last_name = Column(String)
    manager_age = Column(String)
    manager_salary = Column(BigInteger)
    manager_late_remarks = Column(Integer)
    manager_joining_date = Column(Date)
    manager_increment_amount = Column(BigInteger)
    manager_decrement_amount = Column(BigInteger)
    manager_pending_leaves = Column(Integer)
    manager_leave_approve_status = Column(Boolean)

from pydantic import BaseModel
from datetime import date

class ManagerCreate(BaseModel):
    employee_id: int
    manager_id: int
    manager_first_name: str
    manager_last_name: str
    manager_age: str
    manager_salary: int
    manager_late_remarks: int
    manager_joining_date: date
    manager_increment_amount: int
    manager_decrement_amount: int
    manager_pending_leaves: int
    manager_leave_approve_status: bool

    class Config:
        from_attributes = True
