from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
	path('', include('articles.urls')),
    path('', include('chat.urls')),
    path('', include('leads.urls')),
	path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
