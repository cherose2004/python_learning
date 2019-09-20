# 模拟 navcat 操作
# 1.选择数据库
from sqlalchemy.engine import create_engine
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s21?charset=utf8")
# 2.选择表
# 3.创建查询窗口
from sqlalchemy.orm import sessionmaker
select_db = sessionmaker(engine) # 选中数据库
db_session = select_db() # 已经打开查询窗口
# 4.写入SQL语句
# user = User(name="Alexander.DSB.Li") # == insert into user(`name`) value ("Alexander.DSB.Li")
# user_list = [User(name="Alex's Father"),User(name="李杰")]
# 放入查询窗口
# db_session.add(user)
# db_session.add_all(user_list)
# 5.提交sql语句
# db_session.commit()
# 6.关闭查询窗口
# db_session.close()


# 简单无条件查询
# """
# select * from user  table_user == class_User
# """
# res = db_session.query(User).all() # 查询全部符合条件的数据
# res = db_session.query(User).first() # 查询符合条件的第一条数据
# print(res.id,res.name)

# 简单条件查询
# """
# select * from user where id=3
# """
# res = db_session.query(User).filter(User.id==3).all()
# print(res[0].id,res[0].name)
# res = db_session.query(User).filter_by(id=3).all()

# res = db_session.query(User).filter(User.id==3 , User.name == "123").all()
# print(res)
#
# is_true_or_false = User.id==3 and User.name == "123"


# 修改数据 update
# res = db_session.query(User).filter(User.id == 1).update({"name":"李亚历山大"})
# db_session.commit()
# db_session.close()

# 删除数据
# res = db_session.query(User).filter(User.id == 2).delete()
# db_session.commit()
# db_session.close()



