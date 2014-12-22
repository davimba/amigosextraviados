from django.conf.urls import patterns, include, url
from django.contrib import admin

from usuario.urls import routerUsuarioRUD, urlCrearUsuario

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amigosExtraviados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/crear/', include(urlCrearUsuario)),
    url(r'^api/', include(routerUsuarioRUD.urls)),



    #urls temporales para el login y el logout
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),


)
