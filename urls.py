from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoUpload.views.home', name='home'),
    # url(r'^djangoUpload/', include('djangoUpload.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # For the Django Jquery Upload
    (r'^upload/', include('upload.urls')),
    #(r'^upload/', 'upload.views.Upload')),

    #(r'^studyview/', include('studyview.urls')),

)

urlpatterns += staticfiles_urlpatterns()
