from django.urls import path, include
# from watchlist_app.api.views import movies_list, movie_details
from watchlist_app.api.views import StreamPlatformListAV, WatchListAV, WatchDetailAV, StreamPlatformDetailAV

urlpatterns = [
    # path('list/', movies_list, name='movie_list'),
    # path('<int:pk>/', movie_details, name='movie_detail'),
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/', StreamPlatformListAV.as_view(), name = 'stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'stream-detail'),

]