
from django.shortcuts import render

def index_page(req):
    return render(req, 'index.html')
     