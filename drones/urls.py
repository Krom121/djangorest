from django.urls import path
from drones import views 

urlpatterns = [
    # DRONE CAT URLS
    path('drone-categories/',views.DroneCategoryList.as_view(),name=views.DroneCategoryList.name), 
    path('drone-categories/<pk>',views.DroneCategoryDetail.as_view(),name=views.DroneCategoryDetail.name), 
    # DRONE URLS
    path('drones/',views.DroneList.as_view(),name=views.DroneList.name), 
    path('drones/<pk>',views.DroneDetail.as_view(),name=views.DroneDetail.name), 
    # PILOTS URLS
    path('pilots/',views.PilotList.as_view(),name=views.PilotList.name), 
    path('pilots/<pk>',views.PilotDetail.as_view(),name=views.PilotDetail.name), 
    # COMPETITION URLS
    path('competitions/',views.CompetitionList.as_view(),name=views.CompetitionList.name), 
    path('competitions/<pk>',views.CompetitionDetail.as_view(),name=views.CompetitionDetail.name), 
    # API END POINT
    path('',views.ApiRoot.as_view(),name=views.ApiRoot.name), 
]
