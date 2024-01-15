from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import sign_up, sign_in, profile, change_password, logout_request

app_name = 'accounts'

urlpatterns = [
    path('login/', sign_in, name='login'),
    path('register/', sign_up, name='register'),
    path('profile/', profile, name='profile'),
    path('change-password/', change_password, name='change-password'),
    path('logout/', logout_request, name='logout'),
    path('logout/', logout_request, name='logout'),
]


#URL TAMAM
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)