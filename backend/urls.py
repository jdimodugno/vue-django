import backend.views

from django.conf import settings
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve

from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^$', backend.views.index),
    url(r'^beers/$', backend.views.index),
    url(r'^admin/', admin.site.urls),
    # api
    url(r'^api/', include('backend.api.urls')),
    url(r'^tmp/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
