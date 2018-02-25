from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import CommentForm
from .models import Comment


def get_blogs(request):
	ctx = {
		'blogs': Blog.objects.all().order_by('-created')
	}
	return render(request, 'blog/blog-list.html', ctx)


def get_detail(request, pk):
	blog = get_object_or_404(Blog, pk=pk)

	if request.method == 'GET':
		form = CommentForm()
	else:
		form = CommentForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			cleaned_data['blog'] = blog
			Comment.objects.create(**cleaned_data)

	ctx = {
		'blog': blog,
		'comments': blog.comment_set.all().order_by('-created'),
		'form': form,
	}
	return render(request, 'blog/blog-detail.html', ctx)
