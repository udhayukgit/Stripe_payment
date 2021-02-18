from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make_charge_stripe/<int:amount>', views.make_charge_stripe, name='make_charge_stripe'),
]