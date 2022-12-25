import json

from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

from app.forms import PostForm
from app.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()

    json_post_list = serialize("json", post_list)
    object_post_list = json.loads(json_post_list)
    return HttpResponse(json.dumps(object_post_list))


class PostView(View):
    def post(self, request: HttpRequest):
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect("/app/")

    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        post = get_object_or_404(Post, id=id)
        return HttpResponse(post)
