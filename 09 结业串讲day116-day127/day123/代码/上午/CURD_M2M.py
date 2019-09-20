from sqlalchemy.orm import sessionmaker
from app01.static.上午.createM2M import engine

select_db = sessionmaker(engine)
db_session = select_db()

# 增加数据 relationship 正向添加
# g = Girl(name="赵丽颖",gyb=[Boy(name="DragonFire"),Boy(name="冯绍峰")])
# db_session.add(g)
# db_session.commit()
# db_session.close()

# 增加数据 relationship 反向添加
# b = Boy(name="李杰")
# b.byg = [
#     Girl(name="罗玉凤"),
#     Girl(name="朱利安"),
#     Girl(name="乔碧萝")
# ]
#
# db_session.add(b)
# db_session.commit()
# db_session.close()


# 查询 relationship 正向
# res = db_session.query(Girl).all()
# for g in res:
#     print(g.name,len(g.gyb))


# 查询 relationship 反向
# res = db_session.query(Boy).all()
# for b in res:
#     print(b.name,len(b.byg))