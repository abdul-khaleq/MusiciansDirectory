from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addAlbumCreateView.as_view() , name='add_album'),
    path('edit/<int:id>', views.AlbumUpdateView.as_view(), name='edit_album'),
]