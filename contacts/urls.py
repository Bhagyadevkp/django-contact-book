from django.urls import path
from . import views
from .views import ContactDetailView

urlpatterns = [
    path('', views.list_contacts, name='list_contacts'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('create', views.create_contact, name='create_contact'),
    path('<int:pk>/edit/', views.edit_contact, name='edit_contact'),
    path('delete/<int:id>', views.delete_contact, name='delete_contact'),
]