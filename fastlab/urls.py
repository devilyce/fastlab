from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('silvercorp/admin/', admin.site.urls),
                  path('', include('homepage.urls')),
                  path('management/', include('django.contrib.auth.urls')),
                  path('management/', include('datamgt.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('cal/', include('cal.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
