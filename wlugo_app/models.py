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
    email = 
    password = 
    first_name = 
    last_name = 
    program = 
    graduating_year = 
    has_access = 
    is_mod = 
    is_admin = 

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = 
    course_id = 
    body = 
    rating_id = 
    grade = 
    professor_id = 
    term_taken = 
    date_time_created = 

class Professor(models.Model):
    professor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = 
    last_name = 

class Professor_course(models.Model): # ?
    professor = 
    course_id =