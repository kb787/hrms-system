from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Float,
    Boolean,
    Date,
    BigInteger,
)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    age = Column(Integer)
    designation = Column(String(100))
    salary = Column(BigInteger)
    late_remarks = Column(Integer)
    joining_date = Column(Date)
    increment_amount = Column(BigInteger)
    decrement_amount = Column(BigInteger)
    pending_leaves = Column(Integer)
    leave_approve_status = Column(Boolean)
    
from pydantic import BaseModel
from typing import Optional
from datetime import date

class EmployeeCreate(BaseModel):
    employee_id :int
    first_name: str
    last_name: str
    age: int
    designation: str
    salary: float
    joining_date: date
    increment_amount: float
    decrement_amount: float
    pending_leaves: int
    leave_approve_status: Optional[bool] = False

    class Config:
        from_attributes = True  # Replaces old `orm_mode = True`
    
