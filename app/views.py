from django.shortcuts import render

# Create your views here.
def boot_cdn(request):
    return render(request,'boot_cdn.html')



def boot_down(request):
    return render(request,'boot_download.html')