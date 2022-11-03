from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from adoptionrequest.forms import AdoptionrequestForm, AdoptionrequestperpetForm

from adoptionrequest.models import Adoptionrequest, Adoptionrequestperpet


class AdoptionrequestCreateView(CreateView, LoginRequiredMixin):
    template_name = 'adoptionrequest/create_adoptionrequest.html'
    model = Adoptionrequest
    form_class = AdoptionrequestForm
    success_url = reverse_lazy('list_of_adoptionsrequests')


class AdoptionrequestperpetCreateView(CreateView, LoginRequiredMixin):
    template_name = 'adoptionrequest/create_adoptionrequestperpet.html'
    model = Adoptionrequestperpet
    form_class = AdoptionrequestperpetForm
    success_url = reverse_lazy('pets_list')
    #raise_exception = True

    def form_valid(self, form):
        form.instance.poster = self.request.user
        form.save()
        return redirect(self.success_url)

    # def test_func(self):
    #     return self.get_object().poster == self.request.user or self.request.user.is_superuser


class AllRequestsListView(ListView):
    template_name = 'adoptionrequest/list_of_adoptionrequests.html'
    model = Adoptionrequest
    context_object_name = 'all_requests'

    def get_queryset(self):
        return Adoptionrequest.objects.filter(active_of_the_apllicant=True).order_by('-date_time_of_the_apllicant')


class AdoptionrequestDetailView(DetailView):
    template_name = 'adoptionrequest/details_of_adoptionrequest.html'
    model = Adoptionrequest
    success_url = reverse_lazy('list_of_adoptionsrequests')


class AdoptionrequestUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'adoptionrequest/update_adoptionrequest.html'
    model = Adoptionrequest
    form_class = AdoptionrequestForm
    # success_url = reverse_lazy('all_pets')

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def test_func(self):
        return self.get_object().poster == self.request.user or self.request.user.is_superuser


class DeleteadoptionrequestView(UserPassesTestMixin, DeleteView):
    template_name = 'adoptionrequest/delete_adoptionrequest.html'
    model = Adoptionrequest
    success_url = reverse_lazy('list_of_adoptionsrequests')
    raise_exception = True

    # def test_func(self):
    #     return self.get_object().poster == self.request.user or self.request.user.is_superuser

    def test_func(self):
        self.object = self.get_object()
        return self.object.poster == self.request.user or self.request.user.is_superuser

#
# def inactive_adoptionrequest(request, pk):
#     Adoptionrequest.objects.filter(id=pk).update(active=False)
#     return redirect('list_of_adoptionsrequests')