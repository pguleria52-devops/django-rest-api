from django.urls import path, include
# from watchlist_app.api.views import movies_list, movie_details
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import ReviewList, StreamPlatformVS, ReviewCreate, ReviewDetail

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # path('list/', movies_list, name='movie_list'),
    # path('<int:pk>/', movie_details, name='movie_detail'),
    path('', include (router.urls)),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name="review-list"),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    # path('list/', WatchListAV.as_view(), name='movie_list'),
    # path('<int:pk>/', WatchDetailAV.as_view(), name='movie_detail'),
    # path('stream/', StreamPlatformListAV.as_view(), name = 'stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'stream-detail'),
    # path("review/", ReviewList.as_view(), name = 'review-list'),
    # path("review/<int:pk>", ReviewDetail.as_view(), name='review-detail'),

]