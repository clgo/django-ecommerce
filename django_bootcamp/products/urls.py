from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # url(r'^$', TemplateView.as_view(
    #     template_name='products/product_list_view.html')),
    # #url(r'^pk/slug/$', TemplateView.as_view(
    # url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/$', TemplateView.as_view(
    #     template_name='products/product_detail_view.html'),
    # 	name='products_detail_view'),

    url(r'^$', views.ProductListView.as_view(), name='products_list_view'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/$',
    		views.ProductDetailView.as_view(), 
    		name='products_detail_view'),
	]