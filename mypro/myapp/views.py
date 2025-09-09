from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Count

# from django.http import JsonResponse, HttpResponse

from .models import *


class PostsView(View):
    def get(self, request, *args, **kwargs):
        template_name = "myapp/posts.html"

        message = request.session.get("message")
        request.session["message"] = None

        posts = Post.objects.all().annotate(like_count=Count("like"))

        return render(
            request, template_name, {"hello": "hello world", "posts": posts, "message": message}
        )

    def post(self, request, *args, **kwargs):
        print("postリクエスト")
        print(request.POST, request.FILES)

        like = request.POST.get("like")
        if like:
            post_id = like
            post = Post.objects.get(id=post_id)
            request.session["message"] = f"{post.title}の記事にいいねしました。"
            Like.objects.create(post=post)
        else:
            title = request.POST.get("title")
            text = request.POST["text"]

            img = request.FILES.get("img")

            if not title:
                request.session["message"] = "失敗"
                return redirect("myapp:posts")

            print(title, text, immmg)
            print(title, text, immmgggggg)
            Post.objects.create(title=title, text=text, img=img)
            request.session["message"] = "記事の作成に成功しました。"

        return redirect("myapp:post")
        ## ! 本来はこちら↓
        return redirect("myapp:posts")
