from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'employee.views.emp_login'),
    url(r'^logout/$', 'employee.views.emp_logout'),
    url(r'^dashboard/$', 'employee.views.emp_dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)
