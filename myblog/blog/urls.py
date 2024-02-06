from django.urls import path
from . import views
urlpatterns = [
    path("",views.startingpage,name="starting-page"),
    path("posts",views.postspage,name="postspage"),
    path("posts/<slug:slug>",views.postdetailspage,name="postdetails")
]
