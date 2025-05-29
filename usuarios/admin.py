from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
admin.site.register(Usuario, UserAdmin) # é para fazer uma associação de que o model usuario também vai ser usado como usuário admin Customizing the UserAdmin to display additional fields



