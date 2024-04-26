from django.urls import path
from .views import MovieRec

urlpatterns = [
    path('api/movie', MovieRec.as_view(), name='movierec'),
]