from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destinations/', views.destinations, name='destinations'),
    path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),  # Usamos la vista basada en función
    path('destination/add', views.DestinationCreateView.as_view(), name='destination_form'),
    path('destination/<int:pk>/update', views.DestinationUpdateView.as_view(), name='destination_form'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('destination/<int:pk>/delete', views.DestinationDeleteView.as_view(), name='destination_confirm_delete'),
    path('cruise/<int:cruise_id>/', views.cruise_detail, name='cruise_detail'),  # Usamos la vista basada en función
    path('info_request', views.InfoRequestCreate.as_view(), name='info_request'),
]