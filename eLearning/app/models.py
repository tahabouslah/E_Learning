from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    ROLE_CHOICES = [
        ("Student", "Student"),
        ("Tutor", "Tutor"),
        ("Administrator", "Administrator"),
    ]
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    enrollment_capacity = models.IntegerField()


class Enrollment(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrollments"
    )
    enrollment_date = models.DateTimeField(auto_now_add=True)


class Material(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="materials"
    )
    upload_date = models.DateTimeField(auto_now_add=True)
    document_type = models.CharField(max_length=255)


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="assignments"
    )
    due_date = models.DateTimeField()


class Submission(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submissions"
    )
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name="submissions"
    )
    submission_content = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)


class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grades")
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name="grades"
    )
    grade = models.IntegerField()
    feedback = models.TextField(blank=True)


class InteractionHistory(models.Model):
    INTERACTION_TYPE_CHOICES = [
        ("upload", "Upload"),
        ("read", "Read"),
    ]
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interaction_history"
    )
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="interaction_history"
    )
    interaction_type = models.CharField(
        max_length=255, choices=INTERACTION_TYPE_CHOICES
    )
    interaction_date = models.DateTimeField(auto_now_add=True)


class ReadingState(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reading_state"
    )
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="reading_state"
    )
    read_state = models.FloatField()
    last_read_date = models.DateTimeField(auto_now_add=True)
