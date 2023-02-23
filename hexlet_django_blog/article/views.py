from django.shortcuts import render

def index(request):
    return render(request, 'course.html')
                #   , context={
        # 'title': 'Blog',
        # 'subtitle': 'Welcome to the site!',
        # 'body': 'Simple text'})
