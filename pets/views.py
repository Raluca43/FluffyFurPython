# from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

import pets
from adoptionrequest.forms import AdoptionrequestForm, AdoptionrequestperpetForm
from adoptionrequest.models import Adoptionrequest
from pets.forms import PetsForm, UserForm
from pets.models import Pets


class PetsCreateView(CreateView, LoginRequiredMixin):
    template_name = 'pets/create_pets.html'
    model = Pets
    # fields = '__all__'
    form_class = PetsForm
    success_url = reverse_lazy('pets_list')


    def form_valid(self, form):
        form.instance.poster = self.request.user
        form.save()
        return redirect(self.success_url)

#
# class AllPetsListView(ListView):
#     template_name = 'pets/pets_list.html'
#     model = Pets
#     context_object_name = 'all_pets'

#     def __init__(self):
#         super().__init__()
#         self.require_animal = 'dog'
#
#     def get_queryset(self):
#         return Pets.objects.filter(active=True, animal_type=self.require_animal)
#
#     def get(self, request, *args, **kwargs):
#         response = super().get(request, *args, **kwargs)
#         print(request.GET)
#         keys = list(request.GET.keys())
#         first_key = keys[0]
#         self.require_animal = first_key
#         print(first_key)
#         # self.queryset = Pets.objects.filter(animal_type=first_key)
#
#         return response
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         data = super().get_context_data()
#         print(self.require_animal)
#         data['all_pets'] = Pets.objects.filter(animal_type=self.require_animal)
#         return data


def all_pets_view(request):
    print(request.GET)
    keys = list(request.GET.keys())
    if len(keys) > 0:
        first_key = keys[0]
        require_animal = first_key
        print(first_key)
    else:
        require_animal = 'dog'
    pets = Pets.objects.filter(animal_type=require_animal).order_by('-date_time')
    return render(request, 'pets/pets_list.html', {'pets_list': pets})



def pet_details_view(request, pk):
    pet = Pets.objects.get(pk=pk)
    adoptionrequest = AdoptionrequestperpetForm(initial={'pet': pet.id})

    return render(request, 'pets/pet_details.html', {'pets': pet, 'adoptionrequestperpet': adoptionrequest})


class PetUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'pets/update_pet.html'
    model = Pets
    form_class = PetsForm
    # success_url = reverse_lazy('all_pets')

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def test_func(self):
        return self.get_object().poster == self.request.user or self.request.user.is_superuser

class DeletePetView(UserPassesTestMixin, DeleteView):
    template_name = 'pets/delete_pet.html'
    model = Pets
    success_url = reverse_lazy('pets_list')
    raise_exception = True

    # def test_func(self):
    #     return self.get_object().poster == self.request.user or self.request.user.is_superuser

    def test_func(self):
        self.object = self.get_object()
        return self.object.poster == self.request.user or self.request.user.is_superuser

# def inactive_pets(request, pk):
#     Pets.objects.filter(id=pk).update(active=False)
#     return redirect('pets_list')

def search(request):
    searched = ''
    city_pets = []
    if request.method == 'POST':
        searched = request.POST['searched']
        city_pets = Pets.objects.filter(Q(city__icontains=searched) | Q(announce_title__icontains=searched) | Q(animal_type__icontains=searched)
                                        | Q(animal_description__icontains=searched) | Q(animal_label__icontains=searched) | Q(another_label_description__icontains=searched)
                                        | Q(district__icontains=searched) | Q(animal_name__icontains=searched) | Q(gender__icontains=searched)).distinct()
    return render(request, 'pets/search.html', {'searched': searched, 'city_pets': city_pets})



class NewAccountCreateView(CreateView):
    template_name = 'pets/create_new_account.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')


class HomeTemplateView(TemplateView):
    template_name = 'pets/want_to_help.html'