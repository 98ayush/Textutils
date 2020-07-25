from  django.http import  HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def anaylze(request):
    charc = 0
    text1=request.POST.get('text','default')

    removepunc=request.POST.get('remove','default')
    fullcaps = request.POST.get('fullcaps', 'default')
    newlineremover = request.POST.get('newlineremover', 'default')
    if removepunc=="on":
        anaylzed = ""
        punctuation = '''~!@#$%^&*()_+{}":?><'''
        for char in text1:
            if char not in punctuation:
                anaylzed = anaylzed + char
        text1=anaylzed

        params = {'purpose': "remove punctuation", 'anaylzed_text': anaylzed}
        #return render(request, 'anaylze.html', params)
    if fullcaps=="on":
        anaylzed=""
        for char in text1:
            anaylzed=anaylzed+char.upper()
        text1=anaylzed
        params = {'purpose': "Convert to Capital", 'anaylzed_text': anaylzed}
        #return render(request, 'anaylze.html', params)
    if(newlineremover=="on"):
        anaylzed=""
        for char in text1:
            if char!="\n" and char!="\r":
                anaylzed=anaylzed+char
        params = {'purpose': "New line remover", 'anaylzed_text': anaylzed}
        #return render(request, 'anaylze.html', params)
    if newlineremover!="on" and fullcaps!="on" and removepunc!="on":
        return HttpResponse("please select specific option")
    return render(request, 'anaylze.html', params)





