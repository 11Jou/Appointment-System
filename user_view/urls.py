from django.urls import path
from . import views

urlpatterns = [
    path('all_users', views.user_view, name='user_view'),
    path('create_user', views.create_user, name='create_user'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),
    path('edit_user/<int:id>', views.edit_user, name='edit_user'),
]