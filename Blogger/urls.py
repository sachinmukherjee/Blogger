from django.conf.urls import url
from django.contrib import admin
from Blogs import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),

]
