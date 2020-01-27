from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Activity
from .forms import ActivityForm

# Create your views here.
@login_required
def list_activities(request):
    activities = Activity.objects.all()
    return render(request, 'activities.html', {'activities': activities})

@login_required
def new_activity(request):
    form = ActivityForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('list_activities')
    return render(request, 'new_activity.html', {'form': form})

@login_required
def update_activity(request, id):
    activity = get_object_or_404(Activity, pk=id)
    form = ActivityForm(request.POST or None, request.FILES or None, instance=activity)

    if form.is_valid():
        form.save()
        return redirect('list_activities')

    return render(request, 'new_activity.html', {'form': form})

@login_required
def delete_activity(request, id):
    activity = get_object_or_404(Activity, pk=id)

    if request.method == 'POST':
        activity.delete()
        return redirect('list_activities')

    return render(request, 'activity_delete.html', {'activity': activity})
