from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet

# Create the router.
router = SimpleRouter()
# Register the viewset under the desired URL prefix.
router.register("cats", CatViewSet)
# Any number of "URL, viewset" pairs can be registered on the router,
# e.g.:
# router.register('owners', OwnerViewSet)
# but that's not needed here yet.

urlpatterns = [
    # All routes registered on the router are exposed via router.urls;
    # include them in the project's root urlconf.
    path("", include(router.urls)),
]
