from sqlalchemy import Column, String, ForeignKey, Integer, Enum

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Auths(Base):
    __tablename__ = "auths"
    user_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))
    manager_id = Column(Integer, ForeignKey("managers.manager_id"))
    username = Column(String)
    password = Column(String)
    user_role = Column(Enum("employee", "manager", "director"))
