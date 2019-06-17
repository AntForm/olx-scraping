from django.shortcuts import render
from olx.forms import RequestForm
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.

class RequestView(SuccessMessageMixin, FormView):
    template_name = 'olx/request_form.html'
    form_class = RequestForm
    success_url = reverse_lazy('olx')
    success_message = "The result will be sent to your email."
