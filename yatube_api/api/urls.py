from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import PostViewSet, CommentViewSet, GroupListViewSet

app_name = 'api'
API_VER = 'v1'

router = DefaultRouter()
router.register('groups', GroupListViewSet)
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path(f'{API_VER}/', include(router.urls)),
    path(f'{API_VER}/jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path(f'{API_VER}/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path(f'{API_VER}/jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
