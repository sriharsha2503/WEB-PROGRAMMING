from django.shortcuts import render, redirect
from django.http import HttpResponse

def first_page(request):
    if request.method == 'POST':
        # Get form data from the request
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        subject = request.POST.get('subject')
        
        # Store data in session
        request.session['name'] = name
        request.session['roll'] = roll
        request.session['subject'] = subject

        return redirect('second_page')
    return render(request, 'firstPage.html')

def second_page(request):
    # Retrieve data from session
    name = request.session.get('name', '')
    roll = request.session.get('roll', '')
    subject = request.session.get('subject', '')
    
    context = {'name': name, 'roll': roll, 'subject': subject}
    
    if request.method == 'POST':
        return redirect('first_page')
    
    return render(request, 'secondPage.html', context)

