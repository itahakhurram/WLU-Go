from django.db import models
import uuid
# Create your models here.
class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length = 5)
    name = models.CharField(max_length = 20)
    description = models.TextField()
    department = models.CharField(max_length = 20)
    rating_id = models.ForeignKey(Rating, on_delete = models.CSCADE) 
    score = models.FloatField()
    mean_grade = models.FloatField()

class Rating(models.Model):
    rating_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birdness = models.IntegerField(max_length = 1)
    usefulness = models.IntegerField(max_length = 1)
    enjoyability = models.IntegerField(max_length = 1)

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=20)
    password =  models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    program = models.CharField(max_length=20)
    graduating_year = models.IntegerField(max_length=4)
    has_access = models.BooleanField()
    is_mod = models.BooleanField()
    is_admin = models.BooleanField()

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete = models.CSCADE) 
    course_id = models.ForeignKey(Course, on_delete = models.CSCADE) 
    body = models.TextField()
    rating_id = models.ForeignKey(Rating, on_delete = models.CSCADE) 
    grade = models.IntegerField(max_length = 2)
    professor_id = models.ForeignKey(Professor, on_delete = models.CSCADE) 
    term_taken = models.CharField(max_length=20)
    date_time_created = models.DateTimeField()

class Professor(models.Model):
    professor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Professor_course(models.Model): 
    professor_id = models.ForeignKey(Professor, on_delete = models.CSCADE) 
    course_id =models.ForeignKey(Course, on_delete = models.CSCADE) 