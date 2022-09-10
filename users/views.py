from multiprocessing import context
from django.shortcuts import render
from django.http import request
from .models import Profile

# Create your views here.
def profiles(request):
    profile = Profile.objects.all()
    context = {'profile':profile}
    return render(request, 'users/profiles.html', context)

def userprofile(request, pk):
    user = Profile.objects.get(id=pk)

    topskills = user.skill_set.exclude(description__exact="")
    otherskills = user.skill_set.filter(description="")

    context = {'user':user, 'topskills':topskills, 'otherskills':otherskills}
    return render(request, 'users/user-profile.html', context)