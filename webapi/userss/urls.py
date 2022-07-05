from django.urls import path
from .  import views
urlpatterns = [
    path('login/',views.renderlogin,name="login"),
    #path('register/',views.client_registration.as_view(),name="register"),
    path('register/',views.renderregister,name="register"),
    path('logout/',views.logoutuser,name="logout"),
    path('services/',views.services,name="services"),
    path('doctors/<str:choice>/',views.doctors,name="doctors"),
    path('reservation/<str:choice>/',views.renderreservation,name="reservation"),
    path('showreserv/',views.showreserv,name="shovreserv"),
]