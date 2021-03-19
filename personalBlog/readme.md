# Django搭建个人博客
## 项目运行
    一、安装python与Django环境
        1、pip install -r requirement.txt
        2、缺什么补什么
    二、数据库
        1、settings.py 配置数据库
        2、数据库迁移
        python manage.py makegrations
        python manage.py migrate
    三、创建超级管理员账号
        python manage.py createsuperuser
    四、运行
        python manage.py runserver