from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.engine import create_engine

#ORM精髓 relationship
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s21?charset=utf8")
BaseModel = declarative_base()

# 一对多
class School(BaseModel):
    __tablename__ = "school"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)

class Student(BaseModel):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    sch_id = Column(Integer,ForeignKey("school.id"))

    # 关系映射
    stu2sch = relationship("School",backref="sch2stu")


BaseModel.metadata.create_all(engine)




