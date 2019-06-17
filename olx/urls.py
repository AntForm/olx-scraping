from django.urls import path
from django.views.generic import TemplateView
from olx import views

urlpatterns = [
        path('', TemplateView.as_view(template_name="olx/home.html"), name='home'),
        path('olx/', TemplateView.as_view(template_name="olx/olx.html"), name='olx'),
        ]
