from django.shortcuts import render, redirect
from .forms import UploadFileForm, FilterForm
from .models import UploadedFile, Company
from .utils import process_csv

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            process_csv(file.file.path)
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def filter_data(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            filter_field = form.cleaned_data['filter_field']
            results = Company.objects.filter(name__icontains=filter_field)
            return render(request, 'results.html', {'results': results})
    else:
        form = FilterForm()
    return render(request, 'filter.html', {'form': form})