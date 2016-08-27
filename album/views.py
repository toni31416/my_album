from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView


def base(request):
    return render(request, 'base.html')


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class PhotoListView(ListView):
    model = Photo


class PhotoDetailView(DetailView):
    model = Photo


class PhotoUpdate(UpdateView):
    model = Photo
    fields = '__all__'
    
    
class PhotoCreate(CreateView):
    model = Photo
    fields = '__all__'


class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')