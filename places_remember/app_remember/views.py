from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import PlaceForm
from .models import Place


class PlaceView(LoginRequiredMixin, ListView):
    model = Place
    template_name = 'remember/index.html'
    context_object_name = 'places'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreatedPlaceView(LoginRequiredMixin, CreateView):
    form_class = PlaceForm
    template_name = 'remember/place_created.html'
    success_url = reverse_lazy('home')
    raise_exception = True

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = SocialAccount.objects.get(user=self.request.user)
        self.object.auth = user
        self.object.save()
        return super().form_valid(form)


