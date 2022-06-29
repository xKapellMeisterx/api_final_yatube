from django.urls import include, path
from rest_framework_simplejwt import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(
    prefix='follow',
    viewset=FollowViewSet,
    basename='follows'
)

jwt_urlpatterns = [
    path('create/', views.TokenObtainPairView.as_view(), name='jwt-create'),
    path('refresh/', views.TokenRefreshView.as_view(), name='jwt-refresh'),
    path('verify/', views.TokenVerifyView.as_view(), name='jwt-verify'),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/jwt/', include(jwt_urlpatterns)),
]
