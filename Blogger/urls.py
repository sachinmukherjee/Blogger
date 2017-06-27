from django.conf.urls import url
from django.contrib import admin
from Blogs import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/', views.loginValidation),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.home),
    url('^home/(?P<blogs_id>[0-9]+)/$', views.blogs, name='individual blog'),

]
