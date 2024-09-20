import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    #queryset = PageVisit.objects.all()
    queryset = PageVisit.objects.filter(path=request.path)
    page_queryset = PageVisit.objects.all()
    my_title = "Family Matters"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryset.count(),
        "total_visit_count": page_queryset.count()
    }
    path = request.path
    print("path", path)
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    my_title = "I head to Delilah"
    my_context = {
        "page_title": my_title
    }
    html_ = """ 
    <!DOCTYPE html>
<html> 
<body>
    <h1>I get off the plane and nothing has changed</h1>
    <h1>{page_title} with all of my ice</h1>
</body>
</html>
""".format(**my_context)
    #html_file_path = this_dir / "home.html"
    #html_ = html_file_path.read_text() 
    return HttpResponse(html_)