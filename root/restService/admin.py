from django.contrib import admin
from restService.models import *

# Register your models here.
admin.site.register([Object, Feed , Author, Links, Results, Genres])
