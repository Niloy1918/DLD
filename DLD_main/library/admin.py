from django.contrib import admin
from library.models import Accounts
# Register your models here.

class AccountsAdmin(admin.ModelAdmin):
    list_display = ["email","username","password","password2"]

admin.site.register(Accounts,AccountsAdmin)