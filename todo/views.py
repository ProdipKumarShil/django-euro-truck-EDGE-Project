# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render
# # Create your views here.

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

# def aboutUs(request):
#   return render(request, 'aboutus.html')

from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')