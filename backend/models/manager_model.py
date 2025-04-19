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
