from django.urls import path


from . import views


urlpatterns = [
   path('', views.index, name="index"),
   path('translate/', views.run_translate, name='run_translate'),
]


