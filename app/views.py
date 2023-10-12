from django.shortcuts import render
from .selected_data import get_graph


# Create your views here.
def home(request):
    if request.method == "POST":
        tehsil = request.POST.get('tehsil')
        graph = get_graph(tehsil.lower())
        return render(request, 'app/data.html', {'graph': graph})
    
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')