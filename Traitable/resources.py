from django.contrib import admin
from .models import Trait, Pub
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
#from .forms import TraitForm

class TraitResource(resources.ModelResource):
	full_trait = Field()

	class Meta:
		model = Trait
		skip_unchanged = True
		report_skipped = False
		fields = ['id', 'genus', 'species', 'ISI', 'fruit_type',]
		export_order = ['id', 'genus', 'species', 'ISI', 'fruit_type',]

	def dehydrate_full_title(self, Trait):
		return '%s genus %s species' (Trait.genus, Trait.species)

#admin.site.register(TraitResource)


#class TraitAdmin(ImportExportModelAdmin):
	#list_display = ('id', 'genus', 'species', 'isi', 'fruit_type')
	#form = TraitForm
	#resource_class = TraitResource
#	pass