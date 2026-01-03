from django.urls import path
from accounts.views import UserProfileView, UserRegistrationView, UserLoginView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),    # New URL
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'), # New URL
]
