from django.urls import path, include
from .views import CourseDetail,CourseListView,StudentApiView,StudentDetailView,TeacherListView, CreateNewUser
# from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns=[
    path('course/', CourseListView.as_view(), name='course'),
    path('students/', StudentApiView.as_view(), name='student'),
    path('course/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('teachers/', TeacherListView.as_view(), name='teacher'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('user/',CreateNewUser.as_view(), name='new_user' ),
    # path("token_login/",obtain_auth_token, name='course'),
]