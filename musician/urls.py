from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addMusicianCreateView.as_view(), name='add_musician'),
    path('delete/<int:id>', views.AlbumDeleteView.as_view(), name='delete_album'),
    path('edit/<int:id>', views.MusicianUpdateView.as_view(), name='edit_musician'),
]