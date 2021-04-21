from django.urls import path

from .models import IwaterAddresses
from .views import IwaterDriverView, IwaterCategoryDetail, IwaterCategoryList, DetailCompany, IwaterCompanyRegion, \
    IwaterAddress, All_in_clusive, OrderStatusСhanges
from iwaterapi import views
#, FooTwo

app_name = "iwaterapi"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('driver/', IwaterDriverView.as_view()),
    path('order_status_changes/', OrderStatusСhanges.as_view()),
    path('company/<str:name>/',  IwaterCompanyRegion.as_view()),
    # path('company_region/<str:name>/', views.company_region),
    path('category/<int:pk>/', IwaterCategoryDetail.as_view()), # получение по id category
    path('category/', IwaterCategoryList.as_view()),
    # path('users/', IwaterUsers.as_view()),
    path('addresses/<int:pk>/', IwaterAddress.as_view()), #client_id
    path('companyregion/<str:name>/', IwaterCompanyRegion.as_view()),
    # path('iwater_client/', IwaterClient.as_view()),
    path('all_info/', All_in_clusive.as_view()),
    # path('userscateegory/', FooTwo.as_view()),
]

