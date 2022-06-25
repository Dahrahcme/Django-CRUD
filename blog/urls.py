from django.urls import path
from xml.etree.ElementInclude import include
from .views import PostListView
from .views import PostCreateView
from .views import PostDetailView
from .views import PostUpdateView
from .views import PostDeleteView

app_name = "blog"

urlpatterns = [
    path("",PostListView.as_view(), name="all"),
    path("create/",PostCreateView.as_view(), name="post_create"),
    path("delete/<slug:slug>",PostDeleteView.as_view(), name="post_delete"),
    path("update/<slug:slug>",PostUpdateView.as_view(), name="post_update"),
    path("read/<slug:slug>",PostDetailView.as_view(), name="post_detail"),

]
