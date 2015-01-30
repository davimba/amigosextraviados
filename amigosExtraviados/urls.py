from django.conf.urls import patterns, include, url
from django.contrib import admin

from usuario.urls import routerUsuario

from perdido.urls import routerPerdido

from comentario.urls import routerComentario

from notificacion.urls import routerNotificacion
import notifications


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amigosExtraviados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/user/', include(routerUsuario)),
    url(r'^api/perdido/', include(routerPerdido)),

    url(r'^api/comment/', include(routerComentario)),
    url(r'^api/notify/', include(routerNotificacion)),


    #urls temporales para el login y el logout
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^inbox/notifications/', include(notifications.urls)),
    url(r'^api/auth/token/', 'rest_framework_jwt.views.obtain_jwt_token'),

)


from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
