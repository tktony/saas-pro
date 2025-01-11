import pathlib
from django.shortcuts import render # this render function exist in django.http also but it is a convention to use it from shortcuts
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent # returns the current dir (tonhome)

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Pageoo "
    my_context = {
        "page_title": my_title, 
        "page_visit_count": page_qs.count(), 
        "total_visit_count": qs.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)

def my_old_home_page_view(request, *args, **kwargs):
    # string substitution example below
    my_title = "My Page "
    my_context = {
        "page_title": my_title
    }
    html_ = """
        <!DOCTYPE html>
    <html>
        <body>
            <h1>{page_title}This is this real?</h1>
        </body>
    </html>
    """.format(**my_context) # page_title=my_title
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)