from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

class BackPacks(LoginRequiredMixin, generic.CreateView):
	template_name='backpacks/bags.html'
