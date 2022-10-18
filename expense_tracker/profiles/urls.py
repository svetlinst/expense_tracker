from django.urls import path

from expense_tracker.profiles.views import create_profile, show_profile, edit_profile, delete_profile

urlpatterns = (
    path('create/', create_profile, name='create_profile'),
    path('', show_profile, name='show_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_profile, name='delete_profile'),
)