from django.conf.urls import include, url, patterns
from polls.urls import router
# from django.contrib import admin
# from django.conf.urls import patterns, include, url

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'djstatsd.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# ]

urlpatterns = patterns('',
    url(r'^api', include(router.urls)),
)

