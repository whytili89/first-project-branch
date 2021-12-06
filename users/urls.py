from django.urls import path, include

from .views      import SignUpView, SignInView
from .views      import UserProfileView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/<int:user_id>', UserProfileView.as_view())
]