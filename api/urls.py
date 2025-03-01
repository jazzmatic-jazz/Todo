from django.urls import path
from .views.todo import ListTodoAPI, CreateToDoAPI, DetailTodoApi, UpdateDeleteToDoApi
from .views.auth import RegisterAPI, LoginAPI


urlpatterns = [
    path("register", RegisterAPI.as_view(), name="register"),
    path("", ListTodoAPI.as_view(), name="list"),
    path("create", CreateToDoAPI.as_view(), name="create"),
    path("detail/<int:pk>", DetailTodoApi.as_view(), name="detail"),
    path("up-del/<int:pk>", UpdateDeleteToDoApi.as_view(), name="update_delete"),
]
