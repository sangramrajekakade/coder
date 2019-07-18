from django.contrib import admin

from .models import *
from .forms import *

admin.site.register(Post)
admin.site.register(Contact)
class Contact( admin.ModelAdmin ):
    form = ContactForm
admin.site.register(Projects)
