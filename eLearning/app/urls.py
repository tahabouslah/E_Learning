from django.urls import path, include
from .views import *

urlpatterns = [
    # USER
    path("users/", user_list, name="user-list"),
    path("user/<int:pk>/", user_detail, name="user-detail"),
    # COURSE
    path("courses/", course_list, name="course_list"),
    path("course/<int:pk>/", course_detail, name="course-detail"),
    # READINGSTATE
    path("readingStates/", readingState_list, name="readingState_list"),
    path("readingState/<int:pk>/", readingState_detail, name="readingState_detail"),
    # INTERACTIONHISTORY
    path(
        "interactionHistories/", interactionHistory_list, name="interactionHistory_list"
    ),
    path(
        "interactionHistory/<int:pk>/",
        interactionHistory_detail,
        name="interactionHistory_detail",
    ),
    # GRADE
    path("grades/", grade_list, name="grade_list"),
    path("grade/<int:pk>/", grade_detail, name="grade_detail"),
    # SUBMISSION
    path("submissions/", submission_list, name="submission_list"),
    path("submission/<int:pk>/", submission_detail, name="submission_detail"),
    # ASSIGNMENT
    path("assignments/", assignment_list, name="assignment_list"),
    path("assignment/<int:pk>/", assignment_detail, name="assignment_detail"),
    # MATERIAL
    path("materials/", material_list, name="material_list"),
    path("material/<int:pk>/", material_detail, name="material_detail"),
    # ENROLLMENT
    path("enrollment/", enrollment_list, name="enrollment_list"),
    path("enrollment/<int:pk>/", enrollment_detail, name="enrollment_detail"),
]
