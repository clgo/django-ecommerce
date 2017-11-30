from django.conf.urls import url, include
#from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'^shipping-address/$', TemplateView.as_view(
    #     template_name='users/user_shipping_address_view.html')),

    url(r'^shipping-address/$',
    	views.ShippingAddressView.as_view(),
    	name='user_shipping_address_view'),
]