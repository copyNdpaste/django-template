import jwt
from mysite.settings import SIMPLE_JWT


def jwt_authenticator(fn):
    def wrapper(self, request):
        jwt_token = request.headers["Authorization"]
        decoded_jwt = jwt.decode(
            jwt=jwt_token,
            key=SIMPLE_JWT["SIGNING_KEY"],
            algorithms=SIMPLE_JWT["ALGORITHM"],
        )
        user_id = decoded_jwt["user_id"]

        return fn(self, request, user_id=user_id)

    return wrapper
