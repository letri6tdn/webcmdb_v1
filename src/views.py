from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def home_page(request):
	my_title = "Welcome to WebCMDB V1"
	return render(request, "home.html", {"title": my_title})