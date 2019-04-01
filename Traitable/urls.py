from django.conf.urls import url
from traits.views import TraitCreateView, export_traits_csv

urlpatterns = [
    url(r'^trait/create/$', TraitCreateView.as_view(success_url = 'successful_upload.html'), name="create trait"),
    url(r'^export/csv/$', export_traits_csv, name='export_traits_csv'),

]
