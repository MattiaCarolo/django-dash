from django.shortcuts import render

# Create your views here.
def heat(request):
    return render(request, "graph/index.html")