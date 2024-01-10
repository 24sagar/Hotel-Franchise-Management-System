from django.contrib import admin
from services.models import Services

class servicesAdmin(admin.ModelAdmin):
    list_display = ('services_icon','services_title','services_des')
    
admin.site.register(Services,servicesAdmin)
# Register your models here.
