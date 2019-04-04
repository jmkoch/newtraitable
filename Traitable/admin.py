from django.contrib import admin
from .models import Trait, Pub
from import_export.admin import ImportExportModelAdmin
from .resources import TraitResource, PubResource
from .forms import TraitForm, PubForm

class TraitAdmin(ImportExportModelAdmin):
	list_display = ('id', 'genus', 'species', 'isi', 'fruit_type')
	form = TraitForm
	resource_class = TraitResource
#	pass

class TraitInline(admin.TabularInline):
	model = Trait

class PubAdmin(ImportExportModelAdmin):
	list_display = ('title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
	form = PubForm
	resource_class = PubResource
	inlines = [
		TraitInline,
	]

admin.site.register(Trait)
admin.site.register(Pub, PubAdmin)