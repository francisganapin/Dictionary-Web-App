from django.contrib import admin
from django.urls import path, include  # Correct import statement for include
from django.conf.urls.static import static
from django.conf import settings
app_name = 'homepage'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("homepage.urls"))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)