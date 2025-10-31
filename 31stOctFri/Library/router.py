from rest_framework.routers import DefaultRouter
from .views import BookView

library_route=DefaultRouter()

library_route.register(r'book/',BookView)