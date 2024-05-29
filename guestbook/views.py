from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def homepage(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = EntryForm()
    
    
    entries = Entry.objects.all().order_by('-id')
    return render(request, 'guestbook/homepage.html', {'form': form, 'entries': entries})
