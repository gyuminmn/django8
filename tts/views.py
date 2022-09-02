from django.shortcuts import render
from gtts import gTTS

# Create your views here.
def index(request):
    context={}
    if request.method == "POST":
        t = request.POST.get("st")
        f = request.POST.get("fn")
        l = request.POST.get("la")
        gtt = gTTS(t, lang=l)
        gtt.save(f"media/tts/{f}.mp3")
        context.update({
            "st" : t,
            "fn" : f,
            "la" : l,
        })
    return render(request, 'tts/index.html', context)