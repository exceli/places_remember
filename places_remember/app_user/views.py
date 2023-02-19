from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app_remember.models import Place


class ProfileView(LoginRequiredMixin, ListView):
    model = Place
    template_name = 'account/profile.html'
    context_object_name = 'places'
    raise_exception = True

    def get_queryset(self):
        return Place.objects.filter(auth=self.request.user.pk)
