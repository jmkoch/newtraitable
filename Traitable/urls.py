from django.urls import path
from django.conf.urls import url
from .views import TraitCreateView, export_traits_csv

urlpatterns = [
    url(r'^trait/create/$', TraitCreateView.as_view(success_url = 'successful_upload.html'), name="create trait"),
    url(r'^export/traits/csv/$', export_traits_csv, name='export_traits_csv'),
]
