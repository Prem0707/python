from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'books'
    '''
    站点管理汉化
    __init__.py
    
    default_app_config = 'books.apps.BooksConfig'
    '''
    verbose_name = "图书"