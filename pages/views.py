from django.shortcuts import render

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>was gooooooooooood</h1>")
    return render(request, "home.html", {})
