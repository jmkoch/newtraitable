from django.contrib import admin
from .models import Trait, Pub
from import_export.admin import ImportExportModelAdmin
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

#class TraitAdmin(ImportExportModelAdmin):
	#list_display = ('id', 'genus', 'species', 'isi', 'fruit_type')
	#form = TraitForm
	#resource_class = TraitResource
#	pass