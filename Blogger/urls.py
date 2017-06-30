from django.conf.urls import url
from django.contrib import admin
from Blogs import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/(?P<blogs_id>[0-9]+)/$', views.blogs, name='individual blog'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/authenticate/', views.loginValidation),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/addUser/$', views.addUser),
    url(r'^details/$', views.details, name='details'),
    url(r'^details/add_details/', views.detailProcessing),
    url(r'^publish/$', views.publish),
    url(r'^publish/addContent/', views.addContent),



]
