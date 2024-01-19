from django.urls import path
from .views import scrape, display
urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', display, name="display"),
]