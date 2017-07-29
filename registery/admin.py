from django.contrib import admin
from .models import Archive

# Register your models here.
class ArchiveAdmin(admin.ModelAdmin):
	list_display = ['title', 'content', 'timestamp', 'updated',]
	list_filter = ['timestamp']
	search_fields = ['title', 'content']

	class Meta:
		model = Archive


admin.site.register(Archive, ArchiveAdmin)