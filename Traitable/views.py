from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from .models import Trait, Pub
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .resources import TraitResource, PubResource
from tablib import Dataset
from django.contrib.auth.models import User
import csv

# for django-import-export, we need to write a view for every model we're using. 
# Here's the Pub view
class PubCreateView(CreateView):
	model = Pub
	fields = ('id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')

# Trait view
class TraitCreateView(CreateView):
	model = Trait
	fields = ('id', 'genus', 'species', 'isi', 'fruit_type')