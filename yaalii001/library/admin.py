from django.contrib import admin
from library.models import comment,bookdata
# Register your models here.
mdls=(comment,bookdata)
for m in mdls:
    admin.site.register(m)
