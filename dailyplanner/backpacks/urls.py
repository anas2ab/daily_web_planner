from django.urls import path
from . import views

app_name = "backpacks"

urlpatterns = [
	path('bags/', views.BackPacks.as_view(), name='bags')
]