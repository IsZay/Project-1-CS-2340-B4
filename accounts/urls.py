
from . import views


from django.urls import path, include
# from .views import user_login, signup
# from django.contrib.auth.views import LogoutView

#urls is what the urls that we have available,
# as we add new pages, we need to urls, which is the first value in the path function
# the second is basically which function it is going to use from views.py
# the last is basically a field that allow us to see where we are in the website
# name isn't the only thing we can add
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import ForgotPasswordView, ResetConfirm
from .views import ResetComplete


urlpatterns = [
    path('', views.index, name='index'),
    # this should have all of our movie lists together, then have a login button in the top right and a register button.
    # we can have a login button, and there it has a "register here" in there like most websites, which wouldn't be hard to change the path underneath as you'll see ***
    # 'login/register' actually that doesn't make sense
    path('signup/', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),

    # path('forgot/', views.forgot, name='accounts.forgot'),

    path('password_reset/', ForgotPasswordView.as_view(), name='accounts.password_reset'), # Enter your email TODO I CHANGED FROM ForgotPasswordView.as_view()
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), # If real email, sent mail. Now you can go back to home page
         name='accounts.password_reset_done'),
    path('reset/<uidb64>/<token>/',
         ResetConfirm.as_view(), # It starts as a long hex link that verifies who the person who clicked it is. Then once it identifies you, you can change your password
         name='accounts.password_reset_confirm'), #YESSSSSSSSSSS THAT DID IT! CHANGE success_url !!!!!!!!!!

    path('reset/done/',  ResetComplete.as_view(), name='accounts.password_reset_complete'), #pytting include('django.contrib.auth.urls') in 2nd spot also works
    # path('reset/done/', PasswordResetCompleteView.as_view(),
    #      name='accounts.password_reset_complete'), # going to delete  template_name='accounts/password_reset_complete.html'
    # It was inside PasswordResetComlpeteView.as_view(template_name = 'yadda')
    # to see what it should look like
    # or I should overload it, saying ResetComplete.as_view() then
    # in views.py I should make a function called ResetComplete(PasswordResetCompleteView)
    # add in the 4 different fields, and successfully define success_url
    # with the reverse lazy. Maybe
    path('send-test-email/', views.send_test_email, name='send_test_email'),


# path('accounts/', include('django.contrib.auth.urls')),
]
# Now I just need to give the ability for user's to access to there own emails!



