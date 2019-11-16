from django.shortcuts import render
from . import models
import markdown
import pygments
# Create your views here.
def index(request):
    entries = models.Entry.objects.filter(isFeatured=False)
    feature_entries = models.Entry.objects.filter(isFeatured=True)
    return render(request, 'blog/index.html',locals())

def detail(request,blog_id):
    blog_id = blog_id
    entry = models.Entry.objects.get(id=blog_id)
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite'
        ]
    )
    entry.entry_body = md.convert(entry.entry_body)
    return render(request, 'blog/detail.html',locals())