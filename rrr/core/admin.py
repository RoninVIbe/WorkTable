from django.contrib import admin
from .models import Project, Task, Document, Message

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Document)
admin.site.register(Message)


# Register your models here.
