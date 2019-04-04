from django.contrib import admin
from .models import Trait, Pub
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from .forms import TraitForm, PubForm

class PubResource(resources.ModelResource):
	full_pub = Field()

	class Meta:
		model = Pub
		skip_unchanged = True
		report_skipped = False
		fields = ['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type']
		export_order = ['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type']

	def dehydrate_full_pub(self, Pub):
		return '%s lastName %s firstName' % (Pub.lastName, Pub.firstName)

	def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs):
		if 'id' not in dataset.headers:
			dataset.insert_col(0, lambda row: "", header='id')

		print('Here are the columns you will import: ')
		print(dataset.headers)

	def before_save_instance(self, instance, using_transactions, dry_run):
		instance.full_clean()

	def export_pubs_csv(request):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachmnet; filename = "pubs_output.csv"'

		writer = csv.writer(response)
		writer.writerow(['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type'])

		pubs = Pub.objects.all().values_list('id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')

		for pub in pubs:
			writer.writerow(pub)

		return response

class PubAdmin(ImportExportModelAdmin):
	list_display = ('title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
	form = PubForm
	resource_class = PubResource


class TraitResource(resources.ModelResource):
    full_trait = Field()

    class Meta:
        model = Trait
        skip_unchanged = True
        report_skipped = False
        fields = ['id', 'genus', 'species', 'isi', 'fruit_type',]
        export_order = ['id', 'genus', 'species', 'isi', 'fruit_type',]

    def dehydrate_full_title(self, Trait):
        return '%s genus %s species' (Trait.genus, Trait.species)

# before importing csv, this checks for a blank 'id' col. This adds 'id' col if not present
    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs): #raise_errors=True
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: "", header='id')
        print('Here are the columns you will import:' )
        print(dataset.headers)


    def export_traits_csv(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="traits_output.csv"'

        writer = csv.writer(response)
        writer.writerow(['id', 'genus', 'species', 'isi', 'fruit type'])

        traits = Trait.objects.all().values_list('id', 'genus', 'species', 'isi', 'fruit_type')
	    
        for trait in traits:
            writer.writerow(trait)

        return response

class TraitAdmin(ImportExportModelAdmin):
	list_display = ('genus', 'species', 'isi', 'fruit_type')
	form = TraitForm
	resource_class = TraitResource
#	pass