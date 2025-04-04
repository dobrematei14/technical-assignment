from django.shortcuts import render


# Create your views here.
def data_processing_view(request):
    # entries = DataProcessing.objects.all()
    return render(request, 'data_processing/data_list.html')
    # return render(request, 'data_processing/data_list.html', {'entries': entries})
