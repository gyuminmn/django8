from django.shortcuts import render, redirect
from .models import Bookmark

# Create your views here.
def index(request):
    b = Bookmark.objects.all()
    context = {
        "bset" : b
    }
    return render(request, 'book/index.html', context)

def create(request):
    if request.method == "POST":
        sn = request.POST.get('sname')
        su = request.POST.get('surl')
        sc = request.POST.get('scom')
        Bookmark(site_name=sn, url=su, comment=sc).save()
        return redirect('book:index')
    return render(request, 'book/create.html')