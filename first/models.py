from django.db import models


class CustomerRegisterDB(models.Model):
    cname = models.CharField(max_length=55)
    cusername = models.CharField(max_length=55)
    cpassword1 = models.CharField(max_length=55)
    cpassword2 = models.CharField(max_length=55)
    cgmail_id = models.EmailField(max_length=100)
