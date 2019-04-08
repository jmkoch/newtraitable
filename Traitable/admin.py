from django.contrib import admin
from .models import Trait, Pub
from import_export.admin import ImportExportModelAdmin
from .resources import TraitResource, PubResource
from .forms import TraitForm, PubForm

# defining TraitAdmin class (useful & necessary for django-import-export module)
class TraitAdmin(ImportExportModelAdmin):
	list_display = ('id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference')
	form = TraitForm
	resource_class = TraitResource

class TraitInline(admin.TabularInline):
	model = Trait

# defining PubAdmin class (useful & necessary for django-import-export module)
class PubAdmin(ImportExportModelAdmin):
	list_display = ('id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
	form = PubForm
	resource_class = PubResource
	#inlines = [
	#	TraitInline,
	#] # this inline adds Traits to Pub admin page to allow user to upload pub and trait in parallel

class PubInLine(admin.TabularInline):
	model = Pub

# registering our models - very important step!! if you forget to register a model, it won't show up on admin page.
admin.site.register(Trait, TraitAdmin)
admin.site.register(Pub, PubAdmin)