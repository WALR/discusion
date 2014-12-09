from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaDiscusion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.home.urls')),
    url(r'^', include('apps.users.urls', namespace='users')),
    url(r'^', include('apps.discuss.urls', namespace='discuss')),

    #Python Social auth
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
)
