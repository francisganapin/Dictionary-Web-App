from django.urls import path
from .views import dictionary_list,add_dictionary
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dictionary/', dictionary_list, name='dictionary_list'),
    path('dictionary/add/', add_dictionary, name='add-dictionary'),
    
    path('dictionary/edit/<int:id>/', views.edit_dictionary, name='edit_dictionary'),


    path('dictionary/delete/<int:id>/', views.delete_dictionary, name='delete_dictionary'),
    path('', dictionary_list, name='dictionary_list'),
   ]
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)