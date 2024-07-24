from django.shortcuts import render


from django.shortcuts import render

def about(request):
    return render(request, 'pages/about.html')

def staff(request):
    return render(request, 'pages/staff.html')

def contact(request):
    return render(request, 'pages/contact.html')

