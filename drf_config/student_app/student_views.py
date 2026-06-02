# views.py

import json
import jwt
import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User

SECRET_KEY = "mysecretkey"


# ---------------------------------
# ADD USER
# ---------------------------------
@csrf_exempt
def add_user(request):

    if request.method == "POST":

        data = json.loads(request.body)

        user = User.objects.create(
            name=data.get("name"),
            email=data.get("email")
        )

        return JsonResponse({
            "message": "User Added Successfully",
            "id": user.id
        })

    return JsonResponse({
        "message": "Invalid Request"
    }, status=400)


# ---------------------------------
# VIEW ALL USERS
# ---------------------------------
def get_all_users(request):

    if request.method == "GET":

        users = User.objects.all().values()

        return JsonResponse(
            list(users),
            safe=False
        )

    return JsonResponse({
        "message": "Invalid Request"
    }, status=400)


# ---------------------------------
# VIEW USER BY ID
# ---------------------------------
def get_user_by_id(request, id):

    if request.method == "GET":

        try:
            user = User.objects.get(id=id)

            data = {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }

            return JsonResponse(data)

        except User.DoesNotExist:

            return JsonResponse({
                "message": "User Not Found"
            }, status=404)

    return JsonResponse({
        "message": "Invalid Request"
    }, status=400)


# ---------------------------------
# DELETE USER BY ID
# ---------------------------------
@csrf_exempt
def delete_user(request, id):

    if request.method == "DELETE":

        try:
            user = User.objects.get(id=id)

            user.delete()

            return JsonResponse({
                "message": "User Deleted Successfully"
            })

        except User.DoesNotExist:

            return JsonResponse({
                "message": "User Not Found"
            }, status=404)

    return JsonResponse({
        "message": "Invalid Request"
    }, status=400)


# ---------------------------------
# FILTER USER
# Example:
# /user/filter/?name=jeet
# ---------------------------------
def filter_user(request):

    if request.method == "GET":

        name = request.GET.get("name")

        users = User.objects.filter(
            name__icontains=name
        ).values()

        return JsonResponse(
            list(users),
            safe=False
        )

    return JsonResponse({
        "message": "Invalid Request"
    }, status=400)


# ---------------------------------
# CREATE JWT TOKEN
# ---------------------------------
@csrf_exempt
def create_jwt(request):

    if request.method == "POST":

        data = json.loads(request.body)

        payload = {
            "email": data.get("email"),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm="HS256"
        )

        return JsonResponse({
            "token": token
        })

    return JsonResponse({
        "message": "Invalid Request"
    }, status=400)


# ---------------------------------
# VERIFY JWT TOKEN
# ---------------------------------
@csrf_exempt
def verify_jwt(request):

    if request.method == "POST":

        data = json.loads(request.body)

        token = data.get("token")

        try:

            decoded = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

            return JsonResponse({
                "message": "Token Verified",
                "data": decoded
            })

        except jwt.ExpiredSignatureError:

            return JsonResponse({
                "message": "Token Expired"
            }, status=401)

        except jwt.InvalidTokenError:

            return JsonResponse({
                "message": "Invalid Token"
            }, status=401)

    return JsonResponse({
        "message": "Invalid Request"
    }, status=400)