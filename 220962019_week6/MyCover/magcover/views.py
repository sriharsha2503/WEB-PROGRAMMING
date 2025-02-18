# magcover/views.py

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def generate_cover(request):
    cover_image = None
    title = None
    subtitle = None
    background_color = '#FFFFFF'  # default white background
    font_size = '20px'  # default font size
    font_color = '#000000'  # default font color (black)

    if request.method == 'POST':
        # Get the background color, font size, and font color
        background_color = request.POST.get('background_color', '#FFFFFF')
        font_size = request.POST.get('font_size', '20px')
        font_color = request.POST.get('font_color', '#000000')
        title = request.POST.get('title', 'Magazine Title')
        subtitle = request.POST.get('subtitle', 'Subtitle Here')

        # Handle image upload
        if 'cover_image' in request.FILES:
            uploaded_image = request.FILES['cover_image']
            fs = FileSystemStorage()
            cover_image = fs.save(uploaded_image.name, uploaded_image)

    return render(request, 'magcover/generate_cover.html', {
        'cover_image': cover_image,
        'title': title,
        'subtitle': subtitle,
        'background_color': background_color,
        'font_size': font_size,
        'font_color': font_color
    })

