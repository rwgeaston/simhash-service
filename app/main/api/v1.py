from rest_framework.routers import DefaultRouter

from simhash_django.v1.views import HashViewSet

v1_router = DefaultRouter()
v1_router.register(r'hashes', HashViewSet)
