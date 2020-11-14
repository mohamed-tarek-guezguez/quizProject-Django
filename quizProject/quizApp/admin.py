from django.contrib import admin
from .models import Questions1, Questions2

# Register your models here.
class searchAdmin(admin.ModelAdmin):
    search_fields = ('question',)

admin.site.register(Questions1, searchAdmin)
admin.site.register(Questions2, searchAdmin)
