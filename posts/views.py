from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.
def post_create(request):
	return render(request, "post_create.html", {})

def post_list(request):
	object_list = Post.objects.all()
	context = {
		"the_object_list": object_list,
		"title": "List",		
	}
	return render(request, "post_list.html", context)

def post_detail(request):
	detailed_obj = get_object_or_404(Post, id=1)
	context = {
		"detailed_object": detailed_obj,
		"title": "Detail",
	}
	return render(request, "post_detail.html", context)

def post_update(request):
	return HttpResponse("<h1> Update </h1>")

def post_delete(request):
	return HttpResponse("<h1> Delete </h1>")

