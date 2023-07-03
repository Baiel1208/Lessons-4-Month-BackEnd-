from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse

from blog.forms import CommentForm, PostForm
from blog.models import Post, Comment 
from users.models import GeekUser
from django.views import generic
from rest_framework import generics
from blog.serializers import CommentSerializer, PostListSerializer, PostDetailSerializer, UsersListSerializer, UsersDetailSerializer


# hw8
class UsersListAPIView(generics.ListAPIView):
    serializer_class = UsersListSerializer
    queryset = GeekUser.objects.all()


class UsersDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UsersDetailSerializer
    queryset = GeekUser.objects.all()
    lookup_field = "id"


class CommentAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post'])


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.filter(status=True)


class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = "id"


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
    extra_context = {"form": CommentForm()}


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = CommentForm()
    #     return context

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.name = request.user.username
            pre_saved_comment.save()
        return redirect(reverse("post-detail", kwargs={"pk": pk}))


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
    form_class = PostForm
    template_name = "blog/post_create.html"
    # fields = ['title', 'content','cover', "status"]
    success_url = reverse_lazy("index-page")


    # def post(self, request, pk):
	#     post = Post.objects.get(pk=pk)
    #     form = PostForm(request.POST)
    #     return redirect("post-create", pk)

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

# ________________End Update______________________


def get_contacts(request):
    return render(request, "blog/contacts.html")


# def get_about(request):
#     return render(request, "blog/about.html")


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