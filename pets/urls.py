from django.urls import path

from pets import views

urlpatterns = [
    path('create_pets/', views.PetsCreateView.as_view(), name='create_pets'),
    path('', views.all_pets_view, name='pets_list'),
    path('pet_details/<int:pk>/', views.pet_details_view, name='pet_details'),
    path('update_pet/<int:pk>', views.PetUpdateView.as_view(), name='update_pet'),
    path('delete_pet/<int:pk>/', views.DeletePetView.as_view(), name='delete_pet'),
    path('create_new_account/', views.NewAccountCreateView.as_view(), name='create_new_account'),
    path('search/', views.search, name='search'),
    path('want_to_help/', views.HomeTemplateView.as_view(), name='want_to_help'),


]
