"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from api_calls.resource import Add_api_Resource,Provider_Resource,service_area_resource
from api_calls import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


# add_api_resource = Add_api_Resource()
# provider_res=Provider_Resource()
# service_area_res=service_area_resource()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api_calls/', include(add_api_resource.urls)),
    # url(r'^api_calls/', include(provider_res.urls)),
    url(r'^api_calls/test_view', views.test_view.as_view()),
    #url(r'^api_calls/(?P<pk>[0-9]+)/$', views.test_view.as_view()),
    url(r'^api_calls/provider', views.provider.as_view()),
    #url(r'^api_calls/(?P<pk>[0-9]+)/$', views.provider.as_view()),    
    
    #url(r'^api_calls/', include(service_area_res.urls)),
]
