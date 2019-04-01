from import_export import resources
from Traitable.models import Trait, Pub
from import_export.admin import ImportExportModelAdmin
from .forms import TraitForm
from import_export.fields import Field

headers_to_print = []
#expected_headers = ['id', 'genus', 'species', 'isi', 'fruit_type']

class TraitResource(resources.ModelResource):
    full_trait = Field()

    class Meta:
        model = Trait
'''        fields = ['id', 'genus', 'species', 'isi', 'fruit_type']
        export_order = ['id', 'genus', 'species', 'isi', 'fruit_type']
        skip_unchanged = True
        report_skipped = True

    def dehydrate_full_trait(self, Trait):
    	return '%s gen %s spec' % (Trait.genus, Trait.species)

# before importing csv, this checks for a blank 'id' col. This adds 'id' col if not present
    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs): #raise_errors=True
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: "", header='id')
        
        print('Here are the columns you will import:' )
        print(dataset.headers)

#        for key in kwargs:
#        	print("another keyword arg: %s: %s:" % (key, kwargs[key]))  # kwargs 
            # get columns in correct order if user imports incorrectly-formatted csv

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.full_clean()  # i is not a trait object yet; so far it's a tuple with whole dataset
        #print('done')
		# add additional cleaning functions in here (for_delete? etc.)

    def export_traits_csv(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="traits_output.csv"'

        writer = csv.writer(response)
        writer.writerow(['id', 'genus', 'species', 'isi', 'fruit type'])

        traits = Trait.objects.all().values_list('id', 'genus', 'species', 'isi', 'fruit_type')
	    
        for trait in traits:
            writer.writerow(trait)

        return response
'''