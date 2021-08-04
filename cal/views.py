import datetime

from django.http import JsonResponse

from cal.models import setYear, setMonth, setDay, setTime


def get_json_year_data(request):
    year = datetime.datetime.now().year
    qs_year = setYear.objects.filter(name__gte=year).exclude(count__gte=2).values()
    qs_list = list(qs_year)
    return JsonResponse({'data': qs_list})


def get_json_month_data(request, *args, **kwargs):
    selected_year = kwargs.get('year')
    month = datetime.datetime.now().month
    obj_month = list(setMonth.objects.filter(year__name=selected_year, month_number__gte=month).values())
    return JsonResponse({'data': obj_month})


def get_json_day_data(request, *args, **kwargs):
    day = datetime.datetime.now().day
    selected_month = kwargs.get('month')
    obj_day = list(setDay.objects.filter(month__name=selected_month, name__gte=day).values())
    return JsonResponse({'data': obj_day})


def get_json_time_data(request, *args, **kwargs):
    selected_day = kwargs.get('day')
    obj_time = list(setTime.objects.filter(day__name=selected_day).values())
    return JsonResponse({'data': obj_time})
