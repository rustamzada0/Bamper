from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, about, contact, magazine_list, parts_select, result

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('magazine-list/', magazine_list, name='magazine-list'),
    path('parts-select/', parts_select, name='parts-select'),
    path('result/', result, name='result'),
]


#URL TAMAM
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)