from django.urls import path, include
from .views import (
    RegistationCenterAdminApiViewAll, RegistationCenterAdminApiViewInstance, 
    OwnerApiViewAll, OwnerApiViewInstance,
    CarApiViewAll, CarApiViewInstance,
    RegistationDocApiViewAll, RegistationDocApiViewInstance,
    AdminApiViewAll
)

urlpatterns = [
    path('api/center', RegistationCenterAdminApiViewAll.as_view()),
    path('api/center/<int:center_id>/', RegistationCenterAdminApiViewInstance.as_view()),
    path('api/owner', OwnerApiViewAll.as_view()),
    path('api/owner/<int:center_id>/', OwnerApiViewInstance.as_view()),
    path('api/car', CarApiViewAll.as_view()),
    path('api/car/<int:center_id>/', CarApiViewInstance.as_view()),
    path('api/doc', RegistationDocApiViewAll.as_view()),
    path('api/doc/<int:center_id>/', RegistationDocApiViewInstance.as_view()),
    path('api/admin/<int:admin_id>/', AdminApiViewAll.as_view())
]