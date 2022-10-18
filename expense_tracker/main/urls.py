from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from expense_tracker.main.views import show_home, create_expense, edit_expense, delete_expense

urlpatterns = [
                  path('', show_home, name='snow_home'),
                  path('create/', create_expense, name='create_expense'),
                  path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
                  path('delete/<int:expense_id>/', delete_expense, name='delete_expense'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
