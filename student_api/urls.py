from django.urls import path, include
from .views import *

urlpatterns = [
    path("enroll/<int:pk>/", enroll_in_course, name="enroll_in_course"),
    path(
        "grades/<int:student_id>/<int:course_id>/",
        get_grades_and_feedback,
        name="get_grades_and_feedback",
    ),
    path(
        "access-materials/<int:course_id>/",
        access_course_materials,
        name="access_course_materials",
    ),
    path(
        "courses/<int:course_id>/assignments/<int:assignment_id>/submit/",
        submit_assignment,
        name="submit_assignment",
    ),
    path(
        "courses/<int:course_id>/assignments/",
        list_assignments,
        name="list_assignments",
    ),
    path(
        "courses/<int:course_id>/assignments/<int:assignment_id>/",
        get_assignment,
        name="get_assignment",
    ),
]
