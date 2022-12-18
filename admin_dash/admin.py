from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Paper)
admin.site.register(models.Questions)
admin.site.register(models.Answer)