from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, world!')


def path_one(request):
    return HttpResponse('path_one')


def path_page_num(request, page_num):
    return HttpResponse('path_page_num {}'.format(page_num))


def re_path_page_num(request, page_num):
    return HttpResponse('re_path_page_num {}'.format(page_num))
