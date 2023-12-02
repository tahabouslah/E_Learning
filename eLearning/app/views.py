from django.shortcuts import render
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)

# Create your views here.


# COURSE
@api_view(["GET", "POST"])
def user_list(request, format=None):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# COURSE
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def course_list(request):
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAdminUser])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# READINGSTATE
@api_view(["GET", "POST"])
def readingState_list(request):
    if request.method == "GET":
        readingStates = ReadingState.objects.all()
        serializer = ReadingStateSerializer(readingStates, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ReadingStateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def readingState_detail(request, pk):
    try:
        readingState = ReadingState.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(readingState)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ReadingStateSerializer(readingState, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        readingState.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# INTERACTIONHISTORY
@api_view(["GET", "POST"])
def interactionHistory_list(request):
    if request.method == "GET":
        interactionHistories = User.objects.all()
        serializer = InteractionHistorySerializer(interactionHistories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = InteractionHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def interactionHistory_detail(request, pk):
    try:
        interactionHistory = InteractionHistory.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = InteractionHistorySerializer(interactionHistory)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = InteractionHistorySerializer(interactionHistory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        interactionHistory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GRADE
@api_view(["GET", "POST"])
def grade_list(request):
    if request.method == "GET":
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def grade_detail(request, pk):
    try:
        grade = Grade.objects.get(pk=pk)
    except Grade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GradeSerializer(grade)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        grade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SUBMISSION
@api_view(["GET", "POST"])
def submission_list(request):
    if request.method == "GET":
        submissions = Submission.objects.all()
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def submission_detail(request, pk):
    try:
        submission = Submission.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SubmissionSerializer(submission)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SubmissionSerializer(submission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        submission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ASSIGNMENT
@api_view(["GET", "POST"])
def assignment_list(request):
    if request.method == "GET":
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def assignment_detail(request, pk):
    try:
        assignment = Assignment.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# MATERIAL
@api_view(["GET", "POST"])
def material_list(request):
    if request.method == "GET":
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def material_detail(request, pk):
    try:
        material = Material.objects.get(pk=pk)
    except Material.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MaterialSerializer(material)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ENROLLMENT
@api_view(["GET", "POST"])
def enrollment_list(request):
    if request.method == "GET":
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def enrollment_detail(request, pk):
    try:
        enrollment = Enrollment.objects.get(pk=pk)
    except Enrollment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = EnrollmentSerializer(enrollment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        enrollment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes[IsAuthenticated]
def enroll_in_course(request, pk):
    user = request.user
    course = Course.objects.get(id=pk)

    if Enrollment.objects.filter(user=user, course=course).exists():
        return Response(
            {"message": "User is already enrolled in this course."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    enrollment = Enrollment.objects.create(user=user, course=course)

    serializer = EnrollmentSerializer(enrollment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_grades_and_feedback(request, student_id, course_id):
    try:
        student = User.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)
    except User.DoesNotExist:
        return Response(
            {"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Course.DoesNotExist:
        return Response(
            {"message": "Course not found"}, status=status.HTTP_404_NOT_FOUND
        )

    grades = Grade.objects.filter(student=student, assignment__course=course)
    serializer = GradeSerializer(grades, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def access_course_materials(request, course_id):
    user = request.user

    is_enrolled = Enrollment.objects.filter(user=user, course__id=course_id).exists()

    if not is_enrolled:
        return Response(
            {"message": "You are not enrolled in this course."},
            status=status.HTTP_403_FORBIDDEN,
        )

    materials = Material.objects.filter(course__id=course_id)
    serializer = MaterialSerializer(materials, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
