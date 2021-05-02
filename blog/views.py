from django.views import generic
from .models import Post, Comment
from .forms import CommentForm, CustomUserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 3


def post_detail(request, id, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, id=id, slug=slug)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    
    if request.method == 'POST' and request.is_ajax():
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            
            name = request.POST.get('name')
            email = request.POST.get('email')
            body = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, name=name, email=email, body=body, reply=comment_qs)
            comment.save()
            
            
            return JsonResponse({"name": name}, status=200)
        else:
            errors = comment_form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)
    else:
        comment_form = CommentForm()

    context = {'post': post, 'comments': comments, 'comment_form': comment_form}

    # if request.is_ajax():
    #     html = render_to_string('blog/comments.html', context, request=request)
    #     return JsonResponse({'form': html})

    return render(request, template_name, context)
# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST' and request.is_ajax():
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             name = comment_form.cleaned_data['name']
#             # name = request.POST.get('name')
#             # email = request.POST.get('email')
#             # body = request.POST.get('body')
#             # reply_id = request.POST.get('comment_id')
#             # comment_qs = None
#             # if reply_id:
#             #     comment_qs = Comment.objects.get(id=reply_id)
#             # comment = Comment.objects.create(post=post, name=name, email=email, body=body, reply=comment_qs)
#             # comment.save()
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             reply_id = request.POST.get('comment_id')
#             comment_qs = None
#             if reply_id:
#                 comment_qs = Comment.objects.get(id=reply_id)
#             new_comment.reply = comment_qs
#             # Save the comment to the database
#             new_comment.save()
#             return JsonResponse({"name": name}, status=200)
#         else:
#             errors = comment_form.errors.as_json()
#             return JsonResponse({"errors": errors}, status=400)
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'comment_form': comment_form})

def register(request):
    if request.method == "GET":
        return render(request, "registration/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request, user)
            return redirect(reverse("home"))
