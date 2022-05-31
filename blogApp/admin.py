from django.contrib import admin

from .models import Models

# class ModelsAdmin(admin.ModelAdmin):
#     prepopulated_fields={'slug':('title',)}

admin.site.register(Models)

# Register your models here.
