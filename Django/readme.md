python manage.py migrate

python manage.py makemigrations polls
> 相当于 在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动，比如0001_initial.py， 但是这个改动还没有作用到数据库文件

python manage.py sqlmigrate polls 0001
> 显示迁移的SQL语句，具有sqlall的功能

python manage.py migrate
> 将该改动作用到数据库文件，比如产生table之类

python manage.py shell

python manage.py createsuperuser

python manage.py dumpdata myapp > myapp.json
> 数据导出

python manage.py loaddata myapp.json
> 数据导入

python manage.py dumpdata auth > auth.json
> 导出用户数据
