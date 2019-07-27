from django.shortcuts import render

from Questions.models import Questions


# 创建试题的API
def Index(request):
    return render(request, 'index.html')
