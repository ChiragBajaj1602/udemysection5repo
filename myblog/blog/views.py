from django.shortcuts import render

# Create your views here.
def startingpage(request):
    return render(request,"blog/index.html")
def postspage(request):
    pass
def postdetailspage(request,slug):
    pass