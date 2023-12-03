from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from functions.models import Reclamation
from functions.serializers import *


###########################
    ##AUTHENTICATION##
###########################


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response("Logout successful", status=status.HTTP_200_OK)

#############################
    ##CRUD RECLAMATIONS##
#############################

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_reclamation(request):
    if request.user.role not in ['Student', 'Tutor']:
        return Response("This user can't create a reclamation", status=status.HTTP_403_FORBIDDEN)

    serializer = ReclamationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(CustomUser=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liste_reclamtions(request):
    if request.user.role not in ['Studnet','Tutor']:
        return Response("This user has not the permission to CRUD reclamtions" , status=status.HTTP_403_FORBIDDEN)
    reclamations = Reclamation.objects.filter(CustomUser=request.user)
    serializer = ReclamationSerializer(reclamations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_reclamation(request, reclamation_id):
    try :
        reclamation = Reclamation.objects.get(id=reclamation_id)
    except Reclamation.DoesNotExist:
            return Response("This reclamation does not exist",status=status.HTTP_404_NOT_FOUND)
    if request.user != reclamation.CustomUser and request.user.role != "Administrator" :
        return Response("This user is can't delete the reclamation", status=status.HTTP_403_FORBIDDEN)

    reclamation.delete()
    return Response("Reclamation deleted successfully", status=status.HTTP_204_NO_CONTENT)



##########################
    ##CRUD COURSES##
##########################


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_course(request):
    if request.user.role not in ['Tutor','Administrator']:
        return Response("This user can't create a course", status=status.HTTP_403_FORBIDDEN)

    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(tutor=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liste_courses(request):
    if request.user.role not in ['Tutor','Administrator']:
        return Response("This user has not courses" , status=status.HTTP_403_FORBIDDEN)
    courses = Course.objects.filter(tutor=request.user)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response("This course does not exist", status=status.HTTP_404_NOT_FOUND)

    if request.user != course.tutor and request.user.role != "Administrator":
        return Response("This user can't update this course", status=status.HTTP_403_FORBIDDEN)

    serializer = CourseSerializer(course, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_course(request, course_id):
    try :
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
            return Response("This course does not exist",status=status.HTTP_404_NOT_FOUND)
    if request.user != course.tutor and request.user.role != "Administrator" :
        return Response("This user is can't delete this course", status=status.HTTP_403_FORBIDDEN)

    course.delete()
    return Response("Course deleted successfully", status=status.HTTP_204_NO_CONTENT)


##########################
    ##CRUD Materials##
##########################


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_material(request, course_id):
    if request.user.role != 'Tutor':
        return Response("This user can't add a material", status=status.HTTP_403_FORBIDDEN)
    try:
        course = Course.objects.get(id=course_id, tutor=request.user)
    except Course.DoesNotExist:
        return Response("The course which you try to add material don't exist", status=status.HTTP_403_FORBIDDEN)

    serializer = MaterialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(course=course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liste_material(request ,course_id):
    if request.user.role not in ['Tutor','Administrator']:
        return Response("This user has no acces to the material of this course" , status=status.HTTP_403_FORBIDDEN)
    try:
        course = Course.objects.get(id=course_id, tutor=request.user)
    except Course.DoesNotExist:
        return Response("The course which you search don't exist", status=status.HTTP_403_FORBIDDEN)
        
    materials = Material.objects.filter(course=course_id)
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_material(request, course_id , material_id) :
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response("This course does not exist", status=status.HTTP_404_NOT_FOUND)
    try:
        material = Material.objects.get(id=material_id , course=course_id)
    except Material.DoesNotExist :
        return Response("This Material does not exist", status=status.HTTP_404_NOT_FOUND)

    if request.user != course.tutor and request.user.role != "Administrator":
        return Response("This user can't update materials", status=status.HTTP_403_FORBIDDEN)

    serializer = MaterialSerializer(material, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_material(request, course_id , material_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response("This course does not exist", status=status.HTTP_404_NOT_FOUND)
    try:
        material = Material.objects.get(id=material_id , course=course_id)
    except Material.DoesNotExist :
        return Response("This Material does not exist", status=status.HTTP_404_NOT_FOUND)
    
    
    if request.user != course.tutor and request.user.role != "Administrator" :
        return Response("This user can't delete this material", status=status.HTTP_403_FORBIDDEN)

    material.delete()
    return Response("Material deleted successfully", status=status.HTTP_204_NO_CONTENT)


#############################
    ##CRUD Assignements##
#############################


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_assignement(request, course_id):
    if request.user.role != 'Tutor':
        return Response("This user can't add an assignement", status=status.HTTP_403_FORBIDDEN)
    try:
        course = Course.objects.get(id=course_id, tutor=request.user)
    except Course.DoesNotExist:
        return Response("The course which you try to add assignement don't exist", status=status.HTTP_403_FORBIDDEN)

    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(course=course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liste_assignement(request ,course_id):
    if request.user.role not in ['Tutor','Administrator']:
        return Response("This user has no acces to the assignement of this course" , status=status.HTTP_403_FORBIDDEN)
    try:
        course = Course.objects.get(id=course_id, tutor=request.user)
    except Course.DoesNotExist:
        return Response("The course which you search don't exist", status=status.HTTP_403_FORBIDDEN)
        
    assignments = Assignment.objects.filter(course=course_id)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_assignement(request, course_id , assignement_id) :
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response("This course does not exist", status=status.HTTP_404_NOT_FOUND)
    try:
        assignement= Assignment.objects.get(id=assignement_id , course=course_id)
    except Assignment.DoesNotExist :
        return Response("This assignement does not exist", status=status.HTTP_404_NOT_FOUND)

    if request.user != course.tutor and request.user.role != "Administrator":
        return Response("This user can't update assignements", status=status.HTTP_403_FORBIDDEN)

    serializer = AssignmentSerializer(assignement, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_assignement(request, course_id , assignement_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response("This course does not exist", status=status.HTTP_404_NOT_FOUND)
    try:
        assignment = Assignment.objects.get(id=assignement_id , course=course_id)
    except Assignment.DoesNotExist :
        return Response("This assignement does not exist", status=status.HTTP_404_NOT_FOUND)
    
    
    if request.user != course.tutor and request.user.role != "Administrator" :
        return Response("This user can't delete this material", status=status.HTTP_403_FORBIDDEN)

    assignment.delete()
    return Response("assingment deleted successfully", status=status.HTTP_204_NO_CONTENT)


##############################
    ## CRUD ENROLLEMENT##
##############################

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_student(request, course_id , student_id):
    if request.user.role not in ['Tutor','Administrator']:
        return Response("This user can't add a student to a course", status=status.HTTP_403_FORBIDDEN)
    
    try:
        course = Course.objects.get(id=course_id, tutor=request.user)
    except Course.DoesNotExist:
        return Response("The course which you try to add a student don't exist", status=status.HTTP_403_FORBIDDEN)
    
    try:
        student = CustomUser.objects.get(id=student_id, role="Student")
    except CustomUser.DoesNotExist:
        return Response("The student which you try to add to this course don't exist", status=status.HTTP_403_FORBIDDEN)
    
    try:
        enrollment =Enrollment.objects.get(student=student, course=course)
        return Response("This enrollement already exist", status=status.HTTP_403_FORBIDDEN)
    except Enrollment.DoesNotExist:
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course=course ,student=student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_student(request, course_id , student_id):
    
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response("This course does not exist", status=status.HTTP_404_NOT_FOUND)
    try:
        student = CustomUser.objects.get(id=student_id ,role="Student")
    except Assignment.DoesNotExist :
        return Response("This student does not exist", status=status.HTTP_404_NOT_FOUND)
    try:
        enrollment = Enrollment.objects.get(student=student ,course=course)
        
        if request.user != course.tutor and request.user.role != "Administrator" :
            return Response("This user can't delete a enrollement", status=status.HTTP_403_FORBIDDEN)
        enrollment.delete()
        
        return Response("enrollement deleted successfully", status=status.HTTP_204_NO_CONTENT)
    except Enrollment.DoesNotExist :
        
        return Response("This enrollement does not exist", status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liste_enrollement(request ,course_id):
    if request.user.role not in ['Tutor','Administrator']:
        return Response("This user has no acces to the enrollement of this course" , status=status.HTTP_403_FORBIDDEN)
    try:
        course = Course.objects.get(id=course_id, tutor=request.user)
        enrollment = Enrollment.objects.filter(course=course)
        serializer = EnrollmentSerializer(enrollment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        return Response("The course which you search don't exist", status=status.HTTP_403_FORBIDDEN)
        

        