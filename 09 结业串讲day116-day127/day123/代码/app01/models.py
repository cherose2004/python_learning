from app01 import db
# db 全新的SQLAlchemy对象
# db.Model == BaseModel == 使用的SQLAlchemy

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),nullable=False)


if __name__ == '__main__': # 当前文件被当成模块或者是库导入时不会加载一下内容
    from app01 import create_app
    app = create_app()
    db.drop_all(app=app)
    db.create_all(app=app)



