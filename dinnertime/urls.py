from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, url, include

from django.conf import settings # Added by Fiber

from django.contrib import admin
from djrill import DjrillAdminSite

from django.views.generic import TemplateView

# Mandrill Email Support
admin.site = DjrillAdminSite()
admin.autodiscover()

urlpatterns = patterns('',
   # (r'', include('dinnertime.apps.')),
    
    #==========================================================
    # Admin Section 
    #==========================================================
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    #==========================================================
    # End Admin Section
    #==========================================================

    #==========================================================
    # Home Page - Not managed by cms but provided by index.html
    #==========================================================
    url(r'^/?$', TemplateView.as_view(template_name='index.html'), name='home'),
    #==========================================================
    # End Home Page
    #==========================================================

    #==========================================================
    # Userena 
    #==========================================================
    (r'^accounts/', include('userena.urls')),
    #==========================================================
    # End Userena 
    #==========================================================

    #==========================================================
    # Fiber 1 / 2
    #==========================================================
    #(r'^api/v2/', include('fiber.rest_api.urls')),
    #(r'^admin/fiber/', include('fiber.admin_urls')),
    #(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
    #==========================================================
    # End Fiber 1 / 2
    #==========================================================

    #==========================================================
    # Fiber 2 / 2 - Warning this block is a catch all block!!!
    #==========================================================
    #(r'', 'fiber.views.page'),
    #==========================================================

)

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)