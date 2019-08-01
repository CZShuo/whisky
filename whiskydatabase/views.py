import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from whiskydatabase.models import *

def distillery_list():
    distillery_list = Distillery.objects.filter(is_active=True).distinct()
    return {'distillery_list': distillery_list}

class HomeView(ListView):
    model = WhiskyInfo
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DistilleryMapView(TemplateView):
    template_name = "whiskymap.html"

class DistilleryListView(ListView):
    model = Distillery
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DistilleryView(DetailView):
    model = Distillery
    template_name = "home.html"

class WhiskyListView(ListView):
    model = WhiskyInfo
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class WhiskyView(DetailView):
    template_name = "whisky_info.html"
    model = WhiskyInfo
    slug_url_kwarg = "whisky_slug"
    context_object_name = "whisky_detail"

    def get_context_data(self, *args, **kwargs):
        context = super(WhiskyView, self).get_context_data(*args, **kwargs)
        comments = Comment.objects.filter(whisky_id=self.object.id).order_by('created_at')
        personal_note = PersonalWhiskyNote.objects.filter(whisky=self.object).last()
        if personal_note:
            personal_note_array = [personal_note.flora, personal_note.fruity, personal_note.sweet, personal_note.creamy, personal_note.nutty, personal_note.malty, personal_note.salty, personal_note.spicy, personal_note.smoky, personal_note.peaty]
        else:
            personal_note_array = [0,0,0,0,0,0,0,0,0,0]
            
        context.update({
            "comments": comments,
            "personal_note_array":  json.dumps(list(personal_note_array))
        })
        context.update(distillery_list())
        return context