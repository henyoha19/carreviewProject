from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getCarMakes/', views.getCarMakes, name='carmakes'),
    path('getCarModels/', views.getCarModels, name='carmodels'),
    path('carmodeldetails/<int:id>', views.carmodeldetails, name='carmodeldetails'),
    path('newCarMake/', views.newCarMake, name='newcarmake'),
    path('newCarModel/', views.newCarModel, name='newcarmodel'),
    path('logintext/', views.logintext, name='logintext'),
    path('logouttext/', views.logouttext, name='logouttext'),
]