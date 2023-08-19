from django import forms

from contact_form.models import ContactInquiry


class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ["full_name", "phone", "email", "message"]
