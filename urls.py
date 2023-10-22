from django.contrib import admin
from django.urls import path
from Shopello.views import city_views

urlpatterns =[
    path('admin/', admin.site.urls),

    path('cities/', city_views.index, name='cityList'),

    path('cities/create/', city_views.create, name= 'createCity'),

    path('cities/store',city_views.store,name='storeCity'),

    path('cities/edit/<int:pk>',city_views.updateView, name='editCityView'),
    
    path('cities/update/<int:pk>',city_views.update, name='editCity'),

    path('cities/delete/<int:pk>',city_views.delete, name='deleteCity'),
]