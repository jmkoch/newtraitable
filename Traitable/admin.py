from django.contrib import admin
from .models import Trait, Pub
from import_export.admin import ImportExportModelAdmin
from import_export import resources
#from .forms import TraitForm
#from .resources import TraitResource

class TraitInline(admin.TabularInline):
	model = Trait

class PubAdmin(admin.ModelAdmin):
	inlines = [
		TraitInline,
	]

admin.site.register(Trait)
admin.site.register(Pub, PubAdmin)

class TraitResource(resources.ModelResource):

	class Meta:
		model = Trait
		skip_unchanged = True
		report_skipped = False
		fields = ('id', 'genus', 'species', 'ISI', 'fruit_type',)

	def dehydrate_full_title(self, trait):
		return '%s by %s' (trait.genus, trait.species)

#admin.site.register(TraitResource)


#class TraitAdmin(ImportExportModelAdmin):
	#list_display = ('id', 'genus', 'species', 'isi', 'fruit_type')
	#form = TraitForm
	#resource_class = TraitResource
#	pass