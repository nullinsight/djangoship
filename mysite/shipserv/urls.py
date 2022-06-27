from django.urls import path
from . import views

app_name = "shipserv"

urlpatterns = [
    # Asset Management
    path('assetSearch/', views.asset_lookup, name='asset_lookup'),
    path('asset/new/', views.add_asset, name='add_asset'),
    path('asset/return/', views.asset_return, name='asset_return'),
]