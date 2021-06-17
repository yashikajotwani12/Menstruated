from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import ContactForm
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Home/home.html')

class home(ListView):
    template_name='Home/home.html'

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body={
                'first_name':form.cleaned_data['first_name'],
                'last_name':form.cleaned_data['last_name'],
                'email':form.cleaned_data['email'],
                'message':form.cleaned_data['message'],


            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,'admin@example.com',['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("Home:home")
        
    form = ContactForm()
    return render(request, "Home/contact.html", {'form':form})
