from django.urls import path
from .views import ProfileDetailView, UpdateProfileView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'user_profile'

urlpatterns = [
    path('user/<int:user_id>/', ProfileDetailView.as_view(), name='profile'),
    path('user/<int:user_id>/edit', UpdateProfileView.as_view(), name='update_profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

