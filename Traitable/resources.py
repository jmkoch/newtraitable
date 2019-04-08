from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Trait, Pub
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .forms import TraitForm, PubForm

# declaring Pub Resource below (resources are required & helpful for django-import-export module)
# when declaring a model's resource, follow this general setup:
# define class name with parameters (resources.ModelResource):
# then have a line with full_modelName = Field()
# then within the Meta class state the model, the fields to be printed, and the order in which they'll be printed
class PubResource(resources.ModelResource):

	class Meta:
		model = Pub
		skip_unchanged = True  #optional variable that will skip unchanged data imports; DOESNT WORK!!!!
		report_skipped = True #optional variable that will not report skipped imports; DOESNT WORK!!! 
		fields = ['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type']
		export_order = ['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type']

	def dehydrate_full_pub(self, Pub):
		return '%s lastName %s firstName' % (Pub.lastName, Pub.firstName)

	#def dehydrate_citekey(self, Pub):
	#	return Pub.citekey

	# The before_import function will pass some tests prior to importing the data.
	def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs):
		if 'id' not in dataset.headers:
			dataset.insert_col(0, lambda row: "", header='id')

		print('Here are the columns you will import: ')
		print(dataset.headers)

	# Here we will do a simple full_clean of our data before saving it to the database
	def before_save_instance(self, instance, using_transactions, dry_run):
		instance.full_clean()

	# function to export a csv containing all pub data entries
	def export_pubs_csv(request):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachmnet; filename = "pubs_output.csv"'

		writer = csv.writer(response)
		writer.writerow(['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type'])

		pubs = Pub.objects.all().values_list('id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')

		for pub in pubs:
			writer.writerow(pub)

		return response

	#def get_object(self, id):
	#	try:
	#		return Pub.objects.get(pk=citekey)
	#	except Pub.DoesNotExist:
	#		return False

# Trait Resource (for django-import-export)
class TraitResource(resources.ModelResource):
    full_trait = fields.Field(
    	column_name = 'pub_reference',
    	attribute = 'pub_reference',
    	widget = ForeignKeyWidget(Pub, 'citekey')
    )

   # pub_reference = fields.Field(column_name = 'pub_reference', attribute = 'pub_reference', widget=widgets.ForeignKeyWidget(Pub, 'citekey'))

    class Meta:
        model = Trait
        skip_unchanged = True
        report_skipped = False
        fields = ['id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference']
        export_order = ['id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference']

    def dehydrate_full_title(self, Trait):
        return '%s genus %s species' (Trait.genus, Trait.species)

	# before importing csv, this checks for a blank 'id' col. This adds 'id' col if not present
    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs): #raise_errors=True
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: "", header='id')
        
        fields = ['id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference']

# need to fix this; doesn't break but doesn't work; still prints 'Here are the columns you'll import:' and includes bad column (but dosn't upload it)
        for i in fields:
        	if i not in fields:
        		print('We found unrecognized/unexpected data in your csv. Skipping column: '+ str(col_name))
        print('Here are the columns you will import:' )
        print(dataset.headers)

    # function to export all trait entries into a csv
    def export_traits_csv(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="traits_output.csv"'

        writer = csv.writer(response)
        writer.writerow(['id', 'genus', 'species', 'isi', 'fruit type', 'pub_reference'])

        traits = Trait.objects.all().values_list('id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference')
	    
        for trait in traits:
            writer.writerow(trait)

        return response