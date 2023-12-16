from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class addMusicianCreateView(CreateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Musician'
        return context

class AlbumDeleteView(DeleteView):
    model = models.MusicianModel
    template_name = 'delete_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

class MusicianUpdateView(UpdateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update Musician'
        return context