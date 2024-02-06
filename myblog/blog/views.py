from django.shortcuts import render

# Create your views here.
def startingpage(request):
    return render(request,"blog/index.html")
def postspage(request):
    return render(request,"blog/allpost.html")
def postdetailspage(request,slug):
    return render(request,"blog/post-details.html",{
        "postname":slug
    })