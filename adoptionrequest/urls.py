
from django.urls import path

from adoptionrequest import views

urlpatterns = [
    path('create_adoptionrequest/', views.AdoptionrequestCreateView.as_view(), name='create_adoptionrequest'),
    path('create_adoptionrequestperpet/', views.AdoptionrequestperpetCreateView.as_view(), name='create_adoptionrequestperpet'),
    path('list_of_adoptionsrequests/', views.AllRequestsListView.as_view(), name='list_of_adoptionsrequests'),
    path('details_of_adoptionrequest/<int:pk>/', views.AdoptionrequestDetailView.as_view(),
         name='details_of_adoptionrequest'),
    path('update_adoptionrequest/<int:pk>/', views.AdoptionrequestUpdateView.as_view(), name='update_adoptionrequest'),
    path('delete_adoptionrequest/<int:pk>/', views.DeleteadoptionrequestView.as_view(), name='delete_adoptionrequest'),

]
