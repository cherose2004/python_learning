from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

# ORM
# O R M
# Class - Table

# 创建 Class / Table
from sqlalchemy import Column,Integer,String

class User(BaseModel):
    __tablename__ = "user" # 创建Table时名字
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False,index=True,unique=True)
    # Column 定义数据列
    # int string 数据类型

# 数据库引擎的创建:
from sqlalchemy.engine import create_engine
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s21?charset=utf8") # 数据库连接驱动语句

#利用 User 去数据库创建 user Table
BaseModel.metadata.create_all(engine) # 数据库引擎
# 数据库呢? 数据库服务器地址呢?
# 数据库连接呢?
