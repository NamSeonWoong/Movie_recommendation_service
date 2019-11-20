from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('signup/', view.signup, name="signup"),
    path('login/', view.login, name="login"),
    path('logout/', view.logout, name="logout")
]
