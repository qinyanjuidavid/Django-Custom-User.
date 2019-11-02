from django.contrib import admin
from accounts.models import customuser
from accounts.forms import userchangeform, usercreationform

class useradmin(admin.ModelAdmin):
    search_fields=['email',]
    list_display=('email','timestamp','admin')
    list_filter=('admin','staff','active')
    form=userchangeform
    add_form=usercreationform


admin.site.register(customuser, useradmin)
