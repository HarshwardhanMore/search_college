from django.shortcuts import render,redirect
from .models import cutoff
# Create your views here.
def home(request):
    colleges = cutoff.objects.all().order_by('-open_percentile')
    context = {'colleges' : colleges}
    return render(request,'home.html',context=context)

def start(request):
    colleges = cutoff.objects.all().order_by('-open_percentile')
    context = {'colleges' : colleges}
    return render(request,'start.html',context=context) #replace 'testing.html' with 'start.html' 

def search_colleges(request):
    item_searched = 0
    percentile_entered_float=0
    colleges = cutoff.objects.all().order_by('-open_percentile')
    if request.method == 'POST':
        item_searched = request.POST['search']
        percentile_entered = request.POST['percentile_entered']
        percentile_entered_float=0
        if (percentile_entered):
            percentile_entered_float = float(percentile_entered)
        if item_searched:
            colleges = cutoff.objects.filter(college_name__contains=item_searched).order_by('-open_percentile')
        elif (not percentile_entered) & (not item_searched):
            colleges = cutoff.objects.all().order_by('-open_percentile')
            context = {'colleges' : colleges}
            return render(request,'home.html',context=context)

    context = {'colleges' : colleges, 'item_searched': item_searched, 'percentile_entered_float':percentile_entered_float}
    return render(request,'search_colleges.html',context=context)