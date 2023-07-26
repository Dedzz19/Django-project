from django.shortcuts import render
from rest_framework import generics,status,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseSerializer, StudentSerializer,TeacherSerializer,UserSerializer
from .models import Course, Student,Teacher
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAdminUser
# Create your views here.

class CourseListView(APIView):
    def get(self, request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CourseDetail(APIView):
       def get_object(self, id):
            try:
                course=Course.objects.get(id=id)
                return course
            except:
                 raise Http404

       def get(self, request, pk):
            courses= self.get_object(id=pk)
            serializer=CourseSerializer(courses)
            return Response(serializer.data, status=status.HTTP_200_OK)
       
       def put(self, request, pk):
            course = self.get_object(id=pk)
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
       def delete(self, response, pk):
            course=self.get_object(id=pk)
            course.delete()
            return Response("Deleted", status=status.HTTP_204_NO_CONTENT)

class StudentApiView(generics.ListCreateAPIView):
     queryset = Student.objects.all()
     serializer_class= StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Student.objects.all()
     serializer_class= StudentSerializer
     lookup_field="pk"


class TeacherListView(generics.GenericAPIView):
     serializer_class=TeacherSerializer
     queryset=Teacher.objects.all()
     permission_classes=[AllowAny]
     def get(self, request, *args, **kwargs):
        obj=self.get_queryset()
        serializer = self.serializer_class(obj, many=True)
        return Response({"data":serializer.data,'message':"Extra response Message"   }, status=status.HTTP_201_CREATED)
     
     def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response({"success": "Data saved successfully"}, status=status.HTTP_201_CREATED)
        
     
     def get_queryset(self):
         queryset= super().get_queryset()
         category=self.request.query_params.get('course')
         if category is not None:
          queryset=queryset.filter(course__title__icontains=category)
         return queryset
     

class CreateNewUser(generics.CreateAPIView):
     serializer_class=UserSerializer
     queryset=User.objects.all()
     permission_classes=[AllowAny]
     