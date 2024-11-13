from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('accounts/', include([
        path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/profile/'), name='login'),
        path('register/', views.register, name='register'),
    ])),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts/login'), name='logout'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]

api_patterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/UserRegisterView/', views.UserRegisterView.as_view(), name='UserRegisterView'),
    path('token/UserLoginView/', views.UserLoginView.as_view(), name='UserLoginView'),
    path('user/find-users-by-first-name/<str:first_name>/', views.FindUsersByFirstNameView.as_view(), name='FindUsersByFirstNameView'),
    path('user/get-profile-picture/<str:email>/', views.GetProfilePicture.as_view(), name='GetProfilePicture'),
    path('user/EditPhoneNumber/<str:email>/', views.EditPhoneNumber.as_view(), name='EditPhoneNumber'),
    path('session/UserLogoutView/',views.UserLogoutView.as_view(),name='UserLogoutView'),
    path('session/UserSessionLoginView/',views.UserSessionLoginView.as_view(),name='UserSessionLoginView'),
    path('session/CurrentUserView/',views.CurrentUserView.as_view(),name='CurrentUserView')
]