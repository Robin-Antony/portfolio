from django.contrib import admin
from . models import Message, Project,Photo

# Register your models here.
admin.site.register(Message)
admin.site.register(Project)
admin.site.register(Photo)