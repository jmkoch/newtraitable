from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from Traitable.models import Trait, Pub

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from crispy_forms.helper import FormHelper

from django.http import HttpResponse
from traits.resources import TraitResource

from tablib import Dataset
import csv
from django.contrib.auth.models import User

# Trait view 
class TraitCreateView(CreateView):
	model = Trait
	fields = ('id','genus', 'species', 'isi', 'fruit_type')


def simple_upload(request):
    if request.method == 'POST':
        trait_resource = TraitResource()
        dataset = Dataset()
        new_traits = request.FILES['myfile']

        imported_data = dataset.load(new_traits.read())
        result = trait_resource.import_data(dataset, dry_run=True) #test the data import

        if not result.has_errors():
            trait_resource.import_data(dataset, dry_run=False) #now actually import the data

    return render(request, 'core/simple_upload.html')

# code to export the trait csv data from admin (shows up as a button on admin Traits page)
def export_traits_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="traits_output.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'genus', 'species', 'isi', 'fruit type'])

    traits = Trait.objects.all().values_list('id', 'genus', 'species', 'isi', 'fruit_type')
    
    for trait in traits:
        writer.writerow(trait)

    return response


