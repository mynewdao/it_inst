from django.shortcuts import render
from .models import Author

def get_cabinet(request):
    authors = Author.objects.all()
    print(locals())
    return render(request, 'cabinet.html', locals())


def detail_cabinet(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'detail_cabinet.html', locals())
