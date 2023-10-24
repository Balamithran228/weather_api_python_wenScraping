from django.contrib import admin
from first.models import CustomerRegisterDB


class CustomerRegisterAdmin(admin.ModelAdmin):
    customer_register_admin = ['cname', 'cusername', 'cpassword1', 'cpassword2', 'cgmail_id']


admin.site.register(CustomerRegisterDB,CustomerRegisterAdmin)
