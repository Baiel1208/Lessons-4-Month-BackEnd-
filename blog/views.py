from django.shortcuts import render
from blog.models import Post
from django.views import generic
from django.urls import reverse_lazy


# CRUD = Create, Retrieve, Update, Delete


# __________________Retrieve____________________

class IndexListViews(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    template_name = "blog/index.html"


class PostDetailViews(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    

def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def get_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

# ___________________End Retrieve_________________


# _________________Create_________________________

class PostCreateViews(generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ['title', 'content','cover']
    success_url = reverse_lazy("index-page")

# def create_post(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         if title and content:
#             post = Post.objects.create(title=title, content=content)
#             post.save()
#             return reverse_lazy("index-page")
#     return render(request, "blog/post_create.html")

# ___________________End Create_________________


# _________________Delete_________________________
class PostDeleteView(generic.DeleteView):
    model = Post

    success_url = reverse_lazy("index-page")


# ___________________End Delete_________________

# ________________Update__________________________

class PostUpdateViews(generic.UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")


def get_contacts(request):
    return render(request, "blog/contacts.html")


def get_about(request):
    return render(request, "blog/about.html")


def post_update(request, pk):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            post = Post.objects.update(pk=pk, title=title, content=content)

            post.save()
            return reverse_lazy("index-page")

    return render(request, "blog/post_update.html")


def post_delete(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.delete()
    return render(request, "blog/post_delete.html")