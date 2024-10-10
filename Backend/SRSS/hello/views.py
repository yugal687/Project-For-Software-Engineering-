from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World! My Django setup is working.")