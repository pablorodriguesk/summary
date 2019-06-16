from django.contrib import admin
from .models import User
from .models import Summary
from .models import Categoria
# Register your models here.

admin.site.register(User)
admin.site.register(Summary)
admin.site.register(Categoria)
