from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import HiddenInput
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import PlaceForm
from .models import Place


class PlaceView(ListView):
    model = Place
    template_name = 'remember/index.html'
    context_object_name = 'places'
    permission_required = ('app_remember.view_place',)
    paginate_by = 5


class CreatedPlaceView(LoginRequiredMixin, CreateView):
    form_class = PlaceForm
    template_name = 'remember/place_created.html'
    success_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        form = PlaceForm()
        context = super().get_context_data(**kwargs)
        form.fields['address'].widget = HiddenInput()
        context['form'] = form
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = self.request.user
        self.object.auth = user
        self.object.save()
        return super().form_valid(form)


class DetailPlaceView(LoginRequiredMixin, DetailView):
    model = Place
    template_name = 'remember/place_detail.html'
    context_object_name = 'detail'
    slug_url_kwarg = 'detail_slug'
    raise_exception = True

