from django.shortcuts import render
from .models import TrafficVolume


def display_data(request):
    """
    Fetches all entries of TrafficVolume from the database and renders them to 'traffic_data.html'.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: An HttpResponse object that renders the 'traffic_data.html' template
                      displaying all traffic volumes along with the author's name.

    Author:
        Lei Luo
    """
    volumes = TrafficVolume.objects.all()
    return render(request, 'myapp/traffic_data.html', {'data': volumes, 'author': 'Lei Luo'})
