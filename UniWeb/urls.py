from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('WebApp.urls')),
]

admin.site.site_header = "Islamic Call Foundation Admin Panel"
admin.site.site_title="ICF Admin"
admin.site.index_title="Islamic Call Foundation Admin Dashbord "


