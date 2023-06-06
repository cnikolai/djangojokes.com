from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from .models import Joke
from django.urls import reverse_lazy

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer'] # two fields that are presented to the user for creation

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer'] # two fields that are presented to the user for update