from django.shortcuts import render


def main_page(request):
    return render(request, 'mainpage/main-page.html')

def about(request):
    return render(request, 'mainpage/about.html')