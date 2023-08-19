from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactInquiry(models.Model):
    full_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
