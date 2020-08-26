from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return  render(request,'home.html',{})
    
def about(request):
    return  render(request,'about.html',{})
def service(request):
    return  render(request,'service.html',{})
def pricing(request):
    return  render(request,'pricing.html',{})
def blog(request):
    return  render(request,'blog.html',{})

def contact(request):

    if request.method=="POST":
        message_name=request.POST["message-name"]
        message_email=request.POST["message-email"]
        message =request.POST["message"]
        return  render(request,'contact.html',{"message_name":message_name})

        
        # send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
        #  ['elfarah61@gmail.com'], fail_silently=False)

        # #send email
        send_mail(
           message_name, #subject
           message,#message
           message_email,
           ['elfarah61@gmail.com'],
           )#from email
            
             # fail_silently=False)
        

        
    else:
        

        return  render(request,'contact.html',{})