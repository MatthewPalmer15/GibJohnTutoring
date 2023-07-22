from django.shortcuts import render

# Renders the Index (Home) Page to the user
def index(request):
    return render(request, 'main/index.html', {})

# Renders the About Page to the user
def about(request):
    return render(request, 'main/about.html', {})

# Renders the Contact Page to the user
def contact(request):
    return render(request, 'main/contact.html', {})

# Renders the Privacy Policy Page to the user
def policy(request):
    return render(request, 'main/policy.html', {})