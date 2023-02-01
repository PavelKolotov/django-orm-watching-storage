from django.core.exceptions import ObjectDoesNotExist

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.get(passcode=passcode)
    visits_all = Visit.objects.filter(passcard=passcard)
    passcard_visits = []
    for visit in visits_all:
        entered_at = visit.entered_at
        duration = get_duration(visit)
        time_duration = format_duration(duration)
        if duration.seconds > 3600:
            response = True
        else:
            response = False

        this_passcard_visits = {
                'entered_at': entered_at,
                'duration': time_duration,
                'is_strange': response
            }

        passcard_visits.append(this_passcard_visits)

    context = {
        'passcard': passcard,
        'this_passcard_visits': passcard_visits
    }
    return render(request, 'passcard_info.html', context)
