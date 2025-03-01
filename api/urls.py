from django.urls import path
from .views.todo import TodoAPIList, CreateToDo, DetailTodoApi, UpdateToDoApi
from .views.auth import RegisterAPI, LoginAPI


urlpatterns = [
    path("register", RegisterAPI.as_view(), name="register"),
    path("", TodoAPIList.as_view(), name="todo_list"),
    path("create", CreateToDo.as_view(), name="create"),
    path("detail/<int:pk>", DetailTodoApi.as_view(), name="detail"),
    path("up-del/<int:pk>", UpdateToDoApi.as_view(), name="update"),
]
