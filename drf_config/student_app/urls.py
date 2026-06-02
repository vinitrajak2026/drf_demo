from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import student_view,update_student,login_user,user_operation

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
   path("operations",student_view),
    path("update/<int:id>",update_student),
    path("login",login_user),
    path("user",user_operation)
]