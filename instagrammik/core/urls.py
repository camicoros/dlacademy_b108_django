from django.urls import path, re_path
from .views import index, path_one, path_page_num, re_path_page_num

'''
    django проверяет паттерны путей сверху вниз, и вызывает первое совпавшее
    поэтому у нас path_one будет вызываться при url = 1
    path_page_num будет вызван при всех цифровых url кроме 1
    re_path_page_num не будет вызван никогда, пока path_page_num стоит перед ним, 
    т.к. они одинаковые
'''

urlpatterns = [
    path('', index, name='index'),
    path('1/', path_one, name='path_one'),
    path('<int:page_num>/', path_page_num, name='path_page_num'),
    re_path(r'^(?P<page_num>\d+)/$', re_path_page_num, name='re_path_page_num')
]
