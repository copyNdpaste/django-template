from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from accounts.models import User


def login(request: HttpRequest) -> HttpResponse:
    body = request.POST
    username = body["username"]
    password = body["password"]

    user = User.objects.get(username=username)
    is_authenticated = check_password(password, user.password)

    if is_authenticated:
        return HttpResponseRedirect("/api/token/")

    return HttpResponse("로그인 실패")


def signup(request: HttpRequest) -> HttpResponse:
    body = request.POST
    username = body["username"]
    password = body["password"]

    encrypted_password = make_password(password)
    user = User(username=username, password=encrypted_password)
    user.save()

    return HttpResponse("회원가입 성공")
