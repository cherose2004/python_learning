# 启动Flask
from app01 import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
app = create_app()
mig = Migrate(app,db)
manager = Manager(app)
manager.add_command("db",MigrateCommand)
# python manager.py db init 初始化数据库
#
# Flask-Migrate 依赖组件 Flask-Script
"""
数据库迁移指令:
python manager.py db init 
python manager.py db migrate   # Django中的 makemigration
python manager.py db upgrade  # Django中的 migrate
"""

@manager.command
def oldboys21(args):
    print(args)
    return args

@manager.option("-w","--who",dest="who")
@manager.option("-s","--sss",dest="ss")
def func(who,ss):
    print(f"{who},你好{ss}")


if __name__ == '__main__':
    manager.run()
