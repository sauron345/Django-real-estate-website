from django.contrib import admin
from realtors.models import Realtor

# Register your models here.
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25