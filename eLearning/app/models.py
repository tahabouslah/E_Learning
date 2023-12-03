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
    def __str__(self):
        return self.username
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['date_joined']


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    enrollment_capacity = models.IntegerField()
    def __str__(self):
        return self.title
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['title']



class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrollments"
    )
    enrollment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student + ":" + self.course
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        ordering = ['enrollment_date']



class Material(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="materials"
    )
    upload_date = models.DateTimeField(auto_now_add=True)
    document_type = models.CharField(max_length=255)
    def __str__(self):
        return self.title + ":" +self.course
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ['title']



class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="assignments"
    )
    due_date = models.DateTimeField()
    def __str__(self):
        return self.title +":"+self.course
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'
        ordering = ['title']


class Submission(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submissions"
    )
    assignment =  models.OneToOneField(Assignment, on_delete=models.CASCADE)
    submission_content = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student +":"+self.assignment
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'submission'
        verbose_name_plural = 'submissions'
        ordering = ['submission_date']


class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grades")
    assignment =  models.OneToOneField(Assignment, on_delete=models.CASCADE)
    grade = models.IntegerField()
    feedback = models.TextField(blank=True)
    def __str__(self):
        return self.student +":"+self.assignment
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        ordering = ['grade']


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
    def __str__(self):
        return self.student +":"+self.material
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Interaction'
        verbose_name_plural = 'Interactions'
        ordering = ['interaction_date']


class ReadingState(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reading_state"
    )
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="reading_state"
    )
    read_state = models.FloatField()
    last_read_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student +":"+self.material
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'State'
        verbose_name_plural = 'States'
        ordering = ['last_read_date']

class Reclamation(models.Model):
    date_reclam = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reclamation"
    )
    def __str__(self):
        return self.user +":"+self.date_reclam
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'reclamation'
        verbose_name_plural = 'reclamations'
        ordering = ['date_reclam']
    
    
