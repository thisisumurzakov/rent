from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from accounts.views import (
    SignUpView,
    VerifySMSCodeView,
    LogInView,
    LogOutView,
    ForgotPasswordView,
    VerifySMSCodeResetPasswordView,
    ResetPasswordView,
    ChangePhoneNumberView,
    VerifySMSCodeChangePhoneNumberView,
    UserPasswordUpdateView,
    UserProfileUpdateView,
    UserProfileAPIView,
)

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('verify-code/', VerifySMSCodeView.as_view()),
    path('login/', LogInView.as_view()),
    path('logout/', LogOutView.as_view()),
    path("recover/", ForgotPasswordView.as_view(), name="recover"),
    path(
        "verify-code-password/",
        VerifySMSCodeResetPasswordView.as_view(),
        name="verify-code-password",
    ),
    path(
        "reset-password/", ResetPasswordView.as_view(), name="reset_password"
    ),
    path(
        "update-password/",
        UserPasswordUpdateView.as_view(),
        name="update_password",
    ),
    path("change-phone-number/", ChangePhoneNumberView.as_view()),
    path(
        "verify-new-phone-number/",
        VerifySMSCodeChangePhoneNumberView.as_view(),
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("update/", UserProfileUpdateView.as_view(), name="update"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
]