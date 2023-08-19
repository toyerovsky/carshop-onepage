from django.views import generic
from contact_form.forms import ContactInquiryForm

from contact_form.models import ContactInquiry


class Contact(generic.CreateView):
    model = ContactInquiry
    form_class = ContactInquiryForm
    template_name = "contact.html"
    success_url = "/kontakt"
    success_message = "Wiadomość została wysłana!"
