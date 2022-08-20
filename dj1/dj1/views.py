from django.http import HttpResponse

def index(requests):
    return HttpResponse("<h1>SAURABH SAGAR</h1>")

def aboutme(requests):
    return HttpResponse ("<p>yehiihih gig iigdi kigigi khigiu tfddy</p>")

def mycontact(requests):
    return HttpResponse("<h1>DJANGO</h1>")