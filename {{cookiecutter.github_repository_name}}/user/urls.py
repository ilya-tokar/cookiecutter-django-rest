from django.urls import path
from user import views

urlpatterns = [
    path('list/', views.UserList.as_view()),
    path('register/', views.UserCreate.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
]

