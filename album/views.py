from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class addAlbumCreateView(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Album'
        return context

class AlbumUpdateView(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update Album'
        return context