from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import password_reset
from rest_framework import routers
from party import settings
from partyApp.api.views import ProfileViewSet, PartyViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet, base_name='profiles')
router.register(r'parties', PartyViewSet, base_name='parties')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'party.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'partyApp.views.index', name='index'),
    url(r'^user/$', 'partyApp.views.user', name='user'),
    url(r'^event/$', 'partyApp.views.event', name='event'),
    url(r'^admin/', include(admin.site.urls)),

    #api route
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #User account
    url(r'^register/$', 'partyApp.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout',),
    url(r'^user/password/$', password_reset, {'template_name': 'registration/change_password.html'}),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)