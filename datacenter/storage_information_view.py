from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration


def storage_information_view(request):
    visits_now = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for index, visit_now in enumerate(visits_now):
        passcard_name = Passcard.objects.filter(visit=visit_now)[0]
        entered = visits_now[index].entered_at
        duration = get_duration(visits_now[index])
        time_duration = format_duration(duration)
        non_closed_visit = {
                'who_entered': passcard_name,
                'entered_at': entered,
                'duration': time_duration,
            }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
