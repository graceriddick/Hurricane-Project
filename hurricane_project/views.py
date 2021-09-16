# from django.shortcuts import render

# Create your views here.
# def index(request):
#     return render(request, 'index.html')


from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("hurricane_project:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="hurricane_project/register.html", context={"register_form":form})




from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request=request, template_name='hurricane_project/home.html')

def success(request):
	return render(request=request, template_name='hurricane_project/')