from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.views.static import serve

admin.autodiscover()


def custom_server_error(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response


def custom_page_not_found(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response


ROOT_ASSETS = {
    "app/images/": [
        "android-chrome-192x192.png",
        "android-chrome-384x384.png",
        "apple-touch-icon-57x57.png",
        "apple-touch-icon-57x57-precomposed.png",
        "apple-touch-icon-60x60.png",
        "apple-touch-icon-60x60-precomposed.png",
        "apple-touch-icon-72x72.png",
        "apple-touch-icon-72x72-precomposed.png",
        "apple-touch-icon-76x76.png",
        "apple-touch-icon-76x76-precomposed.png",
        "apple-touch-icon-114x114.png",
        "apple-touch-icon-114x114-precomposed.png",
        "apple-touch-icon-120x120.png",
        "apple-touch-icon-120x120-precomposed.png",
        "apple-touch-icon-144x144.png",
        "apple-touch-icon-144x144-precomposed.png",
        "apple-touch-icon-152x152.png",
        "apple-touch-icon-152x152-precomposed.png",
        "apple-touch-icon-180x180.png",
        "apple-touch-icon-180x180-precomposed.png",
        "apple-touch-icon-precomposed.png",
        "apple-touch-icon.png",
        "browserconfig.xml",
        "favicon-16x16.png",
        "favicon-32x32.png",
        "favicon.ico",
        "mstile-150x150.png",
        "safari-pinned-tab.svg",
        "site.webmanifest"
    ]
}

root_assets_urls = []
for prefix, files in ROOT_ASSETS.items():
    for f in files:
        asset_url = staticfiles_storage.url("{prefix}{file}".format(prefix=prefix, file=f))
        root_assets_urls.append(
            url(r'^{0}'.format(f), RedirectView.as_view(url=asset_url))
        )

urlpatterns = [
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^filer/', include('filer.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url('404/$', custom_page_not_found, ),
        url('500/$', custom_server_error, ),
    ]

urlpatterns += i18n_patterns(
    *root_assets_urls,
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^anyball/', admin.site.urls),  # NOQA
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += [
                       url(r'^media/(?P<path>.*)$',
                           serve,
                           {
                               'document_root': settings.MEDIA_ROOT,
                               'show_indexes': True
                           }),
                   ] + staticfiles_urlpatterns()
