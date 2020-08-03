from django.urls import path

from . import views

urlpatterns = [
    path('customer/<int:pk>/users/', views.users_table_view,
         name='users'),
    path('user/<int:pk>/', views.user_detail_view, name='user'),
    path('delete/user/<int:pk>/', views.UserDeleteView.as_view(),
         name='user_delete')
]
