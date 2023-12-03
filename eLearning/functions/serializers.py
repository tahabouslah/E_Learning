from .models import *
from rest_framework import serializers


class ReclamationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamation
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class InteractionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractionHistory
        fields = "__all__"


class ReadingStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingState
        fields = "__all__"
