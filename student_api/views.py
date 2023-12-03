from django.shortcuts import render
from rest_framework import status
from eLearning.app.models import *
from eLearning.app.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(["GET", "POST"])
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


@api_view(["POST"])
def submit_assignment(request, course_id, assignment_id):
    course = get_object_or_404(Course, id=course_id)

    assignment = get_object_or_404(Assignment, id=assignment_id, course=course)

    student = request.user

    if request.method == "POST":
        serializer = SubmissionSerializer(data=request.data)

        if serializer.is_valid():
            if not Enrollment.objects.filter(user=student, course=course).exists():
                return Response(
                    {"error": "Student is not enrolled in the course."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save(student=student, assignment=assignment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_assignments(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    assignments = Assignment.objects.filter(course=course)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_assignment(request, course_id, assignment_id):
    course = get_object_or_404(Course, id=course_id)
    assignment = get_object_or_404(Assignment, id=assignment_id, course=course)
    serializer = AssignmentSerializer(assignment)
    return Response(serializer.data, status=status.HTTP_200_OK)
