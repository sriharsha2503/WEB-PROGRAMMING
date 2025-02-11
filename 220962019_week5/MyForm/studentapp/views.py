from django.shortcuts import render

def index(request):
    # Process form data if any
    if request.method == "POST":
        # Fetch data from the form and process if needed
        pass

    return render(request, 'student_form1.html')

