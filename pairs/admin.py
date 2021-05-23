from django.contrib import admin
from .models import KVPairTable

# Register your models here.
class KVPairAdmin(admin.ModelAdmin):
    list_display = ('time_stamp', 'uuid_val')

admin.site.register(KVPairTable, KVPairAdmin)