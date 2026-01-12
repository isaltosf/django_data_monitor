from django.shortcuts import render

def index(request):
    """Vista principal que renderiza el dashboard"""
    return render(request, 'dashboard/base/base.html')
