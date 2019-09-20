from sqlalchemy.orm import sessionmaker
from app01.static.上午.createForeignKey import engine

select_db = sessionmaker(engine)
db_session = select_db()

# 增加数据
# 先建立一个学校 再查询这个学校的id 利用这个ID 再去创建学生添加sch_id
# relationship 正向添加 relationship字段出现在哪个类
# stu = Student(name="DragonFire",stu2sch=School(name="OldBoyBeijing"))
# stu sql 语句
# db_session.add(stu)
# db_session.commit()
# db_session.close()

# relationship 反向添加
# sch = School(name="OldBoyShanghai")
# sch.sch2stu = [
#     Student(name="赵丽颖"),
#     Student(name="冯绍峰")
# ]
#
# db_session.add(sch)
# db_session.commit()
# db_session.close()


# 查询 relationship 正向
# res = db_session.query(Student).all()
# for stu in res:
#     print(stu.name,stu.stu2sch.name)

# 查询 relationship 反向
# res = db_session.query(School).all()
# for sch in res:
#     # print(sch.name,len(sch.sch2stu)) 学校里面有多少学生
#     for stu in sch.sch2stu:
#         print(sch.name,stu.name)