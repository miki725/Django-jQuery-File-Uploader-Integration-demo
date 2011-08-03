from django.conf.urls.defaults import *

urlpatterns = patterns('upload.views',

    # ================================== #
    #            Upload URLS             #
    # ================================== #

    # Main template with the gui to upload
    # If you want you can expand this so each action of the uploader
    #   will have it's own url. Now a single view is responsible for
    #   distinguishing what it is suppose to do.
    (r'^', 'Upload'),

)
