from django.conf.urls import include, url
from .views import YoMamaBotView
urlpatterns = [
               url(r'^76c5893a5db705c3c7a70f33152ba5d043ce0d9b6ff0835b75/?$', YoMamaBotView.as_view())
               ]