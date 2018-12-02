from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:categoryid>/', views.category),
#    re_path(r'^category/(?P<category>\d+)$', views.category, name='category'),
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product'),
    re_path(r'^contests/$', views.ContestListView.as_view(), name='contests'),
]