from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Human
from django.views.decorators.csrf import csrf_exempt

def human_list(request):
    # Query all Human objects to populate the dropdown list
    humans = Human.objects.all()
    return render(request, 'human_list.html', {'humans': humans})

def get_human(request):
    # This view returns the details for a selected human via AJAX
    human_id = request.GET.get('id')
    if human_id:
        human = get_object_or_404(Human, pk=human_id)
        data = {
            'first_name': human.first_name,
            'last_name': human.last_name,
            'phone': human.phone,
            'address': human.address,
            'city': human.city,
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'No id provided'}, status=400)

@csrf_exempt
def update_human(request):
    # Update the record with new data from the text boxes
    if request.method == 'POST':
        human_id = request.POST.get('id')
        human = get_object_or_404(Human, pk=human_id)
        human.first_name = request.POST.get('first_name')
        human.last_name = request.POST.get('last_name')
        human.phone = request.POST.get('phone')
        human.address = request.POST.get('address')
        human.city = request.POST.get('city')
        human.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt
def delete_human(request):
    # Delete the selected human record
    if request.method == 'POST':
        human_id = request.POST.get('id')
        human = get_object_or_404(Human, pk=human_id)
        human.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid method'}, status=400)

