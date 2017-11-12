from django.conf.urls import url
from django.contrib import admin

from temp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^api/', views.api)
]
