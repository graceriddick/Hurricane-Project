# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index),
# ]



from django.urls import path
from . import views

app_name = "hurricane_project"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register")
]

