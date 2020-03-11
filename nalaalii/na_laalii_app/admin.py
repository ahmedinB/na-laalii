from django.contrib import admin
#f##rom nalaalii.admin_site import custom_admin_site
from .models import mtrlinfo,DEALER,feedback,pro

class BlogPostAdmin(admin.ModelAdmin):
	if DEALER:
		list_display = ('full_name')
	if mtrlinfo:
		list_display = ('frontal_picture')
models=(DEALER,mtrlinfo,feedback,pro)

for m in models: 
	admin.site.register(m)
