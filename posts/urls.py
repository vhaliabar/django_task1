from django.urls import path, include
from .views import FeedDetailView, UserFeedList, home, FeedList
urlpatterns = [    
    path('', home, name='home'),
    path('list/', FeedList.as_view(), name='all_feeds'),
    path('list/<str:user>/', UserFeedList.as_view(), name='user_feeds'),
    path('list/<int:pk>/detail/', FeedDetailView.as_view(), name='feed_detail'),
    
]