import jwt
import datetime
import os


def create_access_token(user):
    payload = {
        "user_id": user["id"],
        "username" : user["username"],
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=int(os.getenv("JWT_ACCESS_EXPIRES")))
    }

    return jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")


def create_refresh_token(user):
    payload = {
        "user_id": user["id"],
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=int(os.getenv("JWT_REFRESH_EXPIRES")))
    }

    return jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")


def decode_token(token):
    secret = os.getenv("SECRET_KEY")

    if not secret:
        print("decode_token error: SECRET_KEY is not set")
        return None

    try:
        print("decode_token token:", token)
        return jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        print("decode_token error: token expired")
        return None
    except jwt.InvalidTokenError as e:
        print("decode_token error: invalid token", str(e))
        return None