"""nalaalii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls.defaults import *
from django.conf.urls import url#,include
from django.urls import re_path, path
from django.contrib import admin
from na_laalii_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # url(r'^detail/(?P<id>[\d]+)',views.sam,name='detail'),
    #url(r'^(?P<key>[\w-]+)/loggedin/$',views.log_in_account,),
    #url(r'^(?P<key>[\w-]+)/registered/$',views.get_account,),
	url(r'^admin/', admin.site.urls),
	url(r'^home/$',views.home,name='home'),
	url(r'^top/',views.top,name='new'),
    url(r'^new/',views.new,name='top'),
	url(r'^news/$',views.news,name='news'),
	url(r'^gojo/',views.gojo,name='gojo'),
    url(r'^services/',views.services,name='services'),
	url(r'^registration/$',views.registration,name='registration'),
    url(r'^categories/$',views.categories,name='categories'),
    url(r'^My_Account/$',views.account,name='account'),
    url(r'^My_Account/logout/$',views.logout,name='logout'),
    url(r'^My_Account/add_asset/$',views.add_asset,),
    url(r'^My_Account/login/$',views.loggedin,name='logged_in'),
    url(r'^My_Account/edit_asset/(?P<desc>[\w%]+)/$',views.edit_asset,),
    url(r'^My_Account/edit_asset/(?P<desc>[\w%]+)/delete/$',views.del_asset,),
    url(r'^registered/$',views.registered,name='registered'),
    url(r'^categories/rooms/',views.rooms,name='home'),
    url(r'^categories/where/$',views.location,name='home'),
    url(r'^categories/sales/$',views.sale,name='home'),
    url(r'^categories/offices/$',views.office,name='home'),
    url(r'^categories/cost/$',views.cost,name='home'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
