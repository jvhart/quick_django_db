
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Quick Django DB Admin Site"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Welcome to the Quick Django DB Admin Site"
