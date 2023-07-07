from django.shortcuts import render
from .models import UserProfile


# Create your views here.


def show_profiles(request):
    context = {"profiles": UserProfile.objects.all(),
               "status": dict(UserProfile.STATUS)}
    return render(request, "profiles.html", context=context)


def show_profile(request, profile):
    context = {"profile": UserProfile.objects.get(pk=profile)}
    return render(request, "profile.html", context=context)


def show_registration_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        age = request.POST.get("age")
        salary = request.POST.get("salary")
        description = request.POST.get("description")

        UserProfile.objects.create(name=name,
                                   surname=surname,
                                   age=age,
                                   salary=salary,
                                   description=description)

    return render(request, "index.html")
