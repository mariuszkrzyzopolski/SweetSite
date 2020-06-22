from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:type_id>', views.offer_list, name='offer_list'),
    path('offer/<int:offer_id>', views.detail, name='detail')
]
