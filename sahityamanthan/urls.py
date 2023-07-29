
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
=======
from django.conf import settings
>>>>>>> 39b1aa2cd7d5e395bd101cb19be1ee8235e2214c
from django.conf.urls.static import static
from django.views.static import server


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('base.urls'))
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]

urlpatterns += staticfiles_urlpatterns()