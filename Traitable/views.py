from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from .models import Trait, Pub
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .resources import TraitResource
from tablib import Dataset
from django.contrib.auth.models import User
import csv

class TraitCreateView(CreateView):
	model = Trait
	fields = ('id', 'genus', 'species', 'isi', 'fruit_type')

def export_traits_csv(request):
	response = HttpResponse(content_type = 'text/csv')
	response['Content-Disposition'] = 'attachment; filename="traits_output.csv"'

	writer = csv.writer(response)
	writer.writerow(['id', 'genus', 'species', 'isi', 'fruit_type'])

	traits = Trait.objects.all().values_list('id', 'genus', 'species', 'isi', 'fruit_type')

	for trait in traits:
		writer.writerow(trait)

	return response