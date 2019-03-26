from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20, default='dummy')
    fist_name = models.CharField(max_length=20, default = 'dummy')
    last_name = models.CharField(max_length=20, default = 'dummy')
    email = models.EmailField(max_length=100)
    role = models.IntegerField(default=0)

    def verifyLogin() -> bool: 
        pass
    
    def editProfile() -> None:
        pass

    def changePassword() -> None:
        pass

    def forgetPassword() -> None:
        pass

    def __str__(self):
        return self.username

class Course(models.Model):
    course_title = models.CharField(max_length=100)
    course_description = models.CharField(max_length=100)
    course_cecu = models.IntegerField()
    course_category = models.IntegerField()

    '''@TODO: There attributes need to be clarified'''
    # course_complete = models.BooleanField()
    # course_completion_date: models.DateTimeField()

    total_completion = models.IntegerField()
    total_current_enrollment = models.IntegerField()


    def enroll_course() -> None:
        pass
    
    def drop_course() -> None:
        pass

    def course_create() -> None:
        pass

    def course_switch() -> None:
        pass

    def add_module() -> None:
        pass

    def course_manage() -> None:
        pass

    def view_course() -> None:
        pass
    
    def show_completion() -> None:
        pass

    def show_enrollment() -> None:
        pass

    def check_course_progress() -> None:
        pass

    def validate_course_pass() -> bool:
        pass

class Learner(User):
    staffID = models.IntegerField()
    obtained_cecu = models.IntegerField()
    enrolled_course = models.ManyToManyField(Course)
    completed_course = models.CharField(max_length=100)

class Instructor(User):
    autobiography = models.CharField(max_length=100)
    teachingCourse = models.ManyToManyField(Course)

    def view_own_course() -> None:
        pass

class Module(models.Model):
    module_title = models.CharField(max_length=100)
    module_complete = models.BooleanField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    module_progress = models.IntegerField()

    #modified from class diagram
    
    def module_create() -> None:
        pass

    def add_component() -> None:
        pass

    def add_quiz() -> None:
        pass

    def module_manage() -> None:
        pass

    def view_module() -> None:
        pass

    def render_component() -> None: #What is this for?
        pass
    
    def render_quiz() -> None:
        pass

    def check_module_progress() -> None:
        pass

    def validate_module_pass() -> bool:
        pass

class Quiz(models.Model):
    quiz_id = models.CharField(max_length=100)
    quiz_number_of_questions = models.IntegerField()
    quiz_passingmark = models.IntegerField()
    quiz_complete = models.BooleanField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default='0', null=True)

    def quiz_create() -> None:
        pass
    
    def quiz_manage() -> None:
        pass
    
    def render_question() -> None:
        pass

    def marks_calculation() -> None:
        pass

    def validate_quiz() -> None:
        pass

class Question(models.Model):
    question = models.CharField(max_length=100)   #str of descriptions?
    choice1 = models.CharField(max_length=100, default=" ")
    choice2 = models.CharField(max_length=100, default=" ")
    choice3 = models.CharField(max_length=100, default=" ")
    choice4 = models.CharField(max_length=100, default=" ")
    answer = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)

    def question_create() -> None:
        pass

    def question_manage() -> None:
        pass

    def validate_answer() -> None:
        pass

class Component(models.Model):
    component_id = models.CharField(max_length=100)
    component_type = models.IntegerField()
    component_title = models.CharField(max_length=100)
    component_creation_date = models.DateTimeField(null=True)
    component_lastUpdate_date = models.DateTimeField(null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)

    def component_create() -> None:
        pass

    def component_manage() -> None:
        pass

    def view_component() -> None:
        pass

class Text(Component):
    component_content = models.CharField(null=True, max_length=100)

class Image(Component):
    component_content = models.ImageField(null=True)






