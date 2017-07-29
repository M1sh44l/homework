from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfuly created a post!")
		return redirect("posts:list")
	context = {
		"title": "Create",
		"form": form,
	}
	return render(request, "post_create.html", context)

def post_list(request):
	object_list = Post.objects.all()#.order_by("-timestamp", "-updated")

	paginator = Paginator(object_list, 10) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		objects = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		objects = paginator.page(paginator.num_pages)

	context = {
		"the_object_list": objects,
		"title": "List",		
	}
	return render(request, "post_list.html", context)

def post_detail(request, post_id):
	detailed_obj = get_object_or_404(Post, id=post_id)
	context = {
		"detailed_object": detailed_obj,
		"title": "Detail",
	}
	return render(request, "post_detail.html", context)

def post_update(request, post_id):
	update_obj = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, instance=update_obj)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully edited post!")
		return redirect(update_obj.get_absolute_url())
	context = {
		"form": form,
		"update_object": update_obj,
		"title": "Update",
	}
	return render(request, "post_update.html", context)


def post_delete(request, post_id):
	delete_obj = get_object_or_404(Post, id=post_id)
	delete_obj.delete()
	messages.success(request, "Successfully deleted!")
	return redirect("posts:list")
