from django.shortcuts import render

def show_main(request):
    context = {
        'name_aplikasi': 'bemostore',
        'name': 'Muhammad Fawwaz Edsa Fatin Setiawan',
        'npm' : '2306275582',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)