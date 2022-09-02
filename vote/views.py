from django.shortcuts import render, redirect
from .models import Topic, Choice

# Create your views here.
def index(request):
    t = Topic.objects.all()
    context = {
        "tset" : t
    }
    return render(request, 'vote/index.html', context)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(request, 'vote/detail.html', context)

def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get('cho')
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
    return redirect('vote:detail', tpk)

def cancel(request,tpk):
    u = request.user
    t = Topic.objects.get(id=tpk)
    t.voter.remove(request.user)
    u.choice_set.get(top=t).choicer.remove(u)
    return redirect('vote:detail', tpk)

def create(request):
    if request.method == "POST":
        s = request.POST.get("top")
        c = request.POST.get("con")
        
        t = Topic(subject=s, content=c, maker=request.user)
        t.save()
        cn = request.POST.getlist("cname")
        cp = request.FILES.getlist("cpic")
        cc = request.POST.getlist("ccom")

        for n,p,c in zip(cn, cp, cc):
            Choice(top=t, name=n, pic=p, content=c).save()
        return redirect("vote:index")
    return render(request, 'vote/create.html')