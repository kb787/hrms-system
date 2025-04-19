from sqlalchemy import String, Integer, Column, Date, Time, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Working(Base):
    __tablename__ = "workings"
    working_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))
    manager_id = Column(Integer, ForeignKey("managers.manager_id"))
    working_date = Column(Date)
    punchin_time = Column(Time)
    punchout_time = Column(Time)
