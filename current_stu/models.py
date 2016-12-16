from __future__ import unicode_literals
from django.db import models

MARITAL_STATUS = (
    ('SINGLE', 'Single'),
    ('MARRIED', 'Married'),
    ('DIVORCED', 'Divorced'),
    ('WIDOWED', 'Widowed'),
)


class StudentInfo(models.Model):
    id = models.AutoField(primary_key=True)

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30, blank=True)
    englishname = models.CharField(max_length=30, blank=True)
    dob = models.DateField()
    birthplace = models.CharField(max_length=50)
    apply_grade = models.CharField(max_length=2)
    start_date = models.DateField()
    visa = models.CharField(max_length=20)
    nation = models.CharField(max_length=50)
    i20 = models.BooleanField()

    def __unicode__(self):
        return self.lastname


class FatherInfo(models.Model):
    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    lastname = models.CharField(max_length=30, blank=True)
    firstname = models.CharField(max_length=30, blank=True)
    marital = models.CharField(max_length=10, choices=MARITAL_STATUS, default='MARRIED', blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    employer = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=50, blank=True)
    day_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


class MotherInfo(models.Model):
    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    lastname = models.CharField(max_length=30, blank=True)
    firstname = models.CharField(max_length=30, blank=True)
    marital = models.CharField(max_length=10, choices=MARITAL_STATUS, default='MARRIED', blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    employer = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=50, blank=True)
    day_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


class ContactInfo(models.Model):
    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    CONTACT_TIME = (
        ('MORNING', 'Mornings'),
        ('AFTERNOON', 'Afternoons'),
        ('EVENING', 'Evenings'),
        ('WEEKDAY', 'Weekdays'),
        ('WEEKEND', 'Weekends'),
    )

    address = models.CharField(max_length=200)
    apt = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    home_phone = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


class AdditionalHousehold(models.Model):
    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    name1 = models.CharField(max_length=50, blank=True)
    gender1 = models.CharField(max_length=6, blank=True)
    relationship1 = models.CharField(max_length=10, blank=True)
    school1 = models.CharField(max_length=50, blank=True)
    age1 = models.IntegerField(blank=True)
    grade1 = models.CharField(max_length=50, blank=True)

    name2 = models.CharField(max_length=50, blank=True)
    gender2 = models.CharField(max_length=6, blank=True)
    relationship2 = models.CharField(max_length=10, blank=True)
    school2 = models.CharField(max_length=50, blank=True)
    age2 = models.IntegerField(blank=True)
    grade2 = models.CharField(max_length=50, blank=True)

    name3 = models.CharField(max_length=50, blank=True)
    gender3 = models.CharField(max_length=6, blank=True)
    relationship3 = models.CharField(max_length=10, blank=True)
    school3 = models.CharField(max_length=50, blank=True)
    age3 = models.IntegerField(blank=True)
    grade3 = models.CharField(max_length=50, blank=True)


class SchoolInfo(models.Model):
    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    currentschool = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    grade = models.IntegerField()
    gpa = models.CharField(max_length=3)
    rank = models.CharField(max_length=50)
    enrolldate = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    post = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField()


class TestScore(models.Model):
    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    slep = models.IntegerField(blank=True)
    slepdate = models.CharField(max_length=20, blank=True)
    toefl = models.IntegerField(blank=True)
    toefldate = models.CharField(max_length=20, blank=True)
    ssat = models.IntegerField(blank=True)
    ssatdate = models.CharField(max_length=20, blank=True)
    sat = models.IntegerField(blank=True)
    satdate = models.CharField(max_length=20, blank=True)
    act = models.IntegerField(blank=True)
    actdate = models.CharField(max_length=20, blank=True)
    other = models.IntegerField(blank=True)
    otherdate = models.CharField(max_length=20, blank=True)


class History(models.Model):
    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    visit = models.CharField(max_length=3)
    when = models.CharField(max_length=255, blank=True)
    long = models.CharField(max_length=50, blank=True)
    reason = models.CharField(max_length=255, blank=True)
    rate = models.CharField(max_length=50, blank=True)


class Profile(models.Model):
    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    role_model = models.CharField(max_length=255)
    dream_job = models.CharField(max_length=255)
    interest = models.CharField(max_length=255)
    hobby = models.CharField(max_length=255)
    current_goal = models.CharField(max_length=255)
    future_goal = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    food = models.CharField(max_length=255)
    music = models.CharField(max_length=255)
    holiday = models.CharField(max_length=255)
    animal = models.CharField(max_length=255)
    movie = models.CharField(max_length=255)
    book = models.CharField(max_length=255)
    weekend = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    happiest = models.CharField(max_length=255)


#######################################################################################


class MultipleChoice(models.Model):

    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    ###############
    # Personality Type
    PERSONALITY = (
        ('CONSERVATIVE', 'Conservative'),
        ('PRIVATE', 'Private'),
        ('OPEN-MINDED', 'Open-minded'),
        ('QUIET', 'Quiet'),
        ('ACTIVE', 'Active'),
        ('LIBERAL', 'Liberal'),
        ('OUTGOING', 'Outgoing'),
        ('SOCIAL', 'Social'),
        ('TRADITIONAL', 'Traditional'),
        ('OTHER', 'Other')
    )
    personality = models.CharField(max_length=20, choices=PERSONALITY, blank=True)

    ###############
    # Eating Habits
    EAT = (
        ('FRUIT', 'Fruits'),
        ('CHICKEN', 'Chicken'),
        ('EGG', 'EGGS'),
        ('NOODLES', 'Noodles'),
        ('RICE', 'Rice'),
        ('MEAT', 'Red Meat'),
        ('VEG', 'Vegetables'),
        ('BREAD', 'Bread/Cereals'),
        ('SOY', 'Soy'),
        ('OR', 'Other')
    )
    eat = models.CharField(max_length=30, choices=EAT, blank=True)

    NOT_EAT = (
        ('FRUIT', 'Fruits'),
        ('CHICKEN', 'Chicken'),
        ('EGG', 'EGGS'),
        ('NOODLES', 'Noodles'),
        ('RICE', 'Rice'),
        ('MEAT', 'Red Meat'),
        ('VEG', 'Vegetables'),
        ('BREAD', 'Bread/Cereals'),
        ('SOY', 'Soy'),
        ('OR', 'Other')
    )
    not_eat = models.CharField(max_length=30, choices=NOT_EAT, blank=True)

    SPECIAL_DIET = (
        ('DAIRY', 'Dairy_Free'),
        ('GLUTEN', 'Gluten_Free'),
        ('VEGETARIAN', 'Vegetarian'),
        ('VEGAN', 'Vegan'),
        ('OR', 'Other')
    )
    special_diet = models.CharField(max_length=20, choices=SPECIAL_DIET, blank=True)

    ALLERGY = (
        ('NUTS', 'Nuts'),
        ('MILK', 'Milk'),
        ('FISH', 'Fish'),
        ('VEGAN', 'Vegan'),
        ('WHEAT', 'Wheat'),
        ('OR', 'Other')
    )
    allergy = models.CharField(max_length=20, choices=ALLERGY, blank=True)

    RESTAURANT = (
        ('CH', 'Chinese'),
        ('KR', 'Korean'),
        ('JP', 'Japanese'),
        ('US', 'American'),
        ('MN', 'Mexican'),
        ('IY', 'Italian'),
        ('OR', 'Other')
    )
    restaurant = models.CharField(max_length=2, choices=RESTAURANT, blank=True)

    OWN_MEAL = (
        ('YES', 'Yes'),
        ('NO', 'No')
    )
    own_meal = models.CharField(max_length=3, choices=OWN_MEAL, blank=True)

    ##############
    # Preferences
    PET = (
        ('CAT', 'Like cats'),
        ('DOG', 'Like dogs'),
        ('ALL', 'Like all animals'),
        ('NO', "Don't like animals")
    )
    pet = models.CharField(max_length=3, choices=PET, blank=True)

    SMOKE = (
        ('YES', 'yes'),
        ('NO', 'no')
    )
    smoke = models.CharField(max_length=3, choices=SMOKE, blank=True)

    SMOKE_FREE = (
        ('YES', 'yes'),
        ('NO', 'no')
    )
    smoke_free = models.CharField(max_length=3, choices=SMOKE_FREE, blank=True)

    RElIGIOUS_SERVICE = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('DCARE', "Don't care")
    )
    religious_service = models.CharField(max_length=10, choices=RElIGIOUS_SERVICE, blank=True)

    WEEKDAY_CURFEW = (
        ('9', '9PM'),
        ('10', '10PM'),
        ('11', '11PM'),
        ('12', '12MM')
    )
    weekday_curfew = models.CharField(max_length=5, choices=WEEKDAY_CURFEW, blank=True)

    WEEKEND_CURFEW = (
        ('11', '11PM'),
        ('12', '12AM'),
        ('1', '1AM'),
        ('2', '2AM')
    )
    weekend_curfew = models.CharField(max_length=5, choices=WEEKEND_CURFEW, blank=True)


#######################################################################################


class ShortAnswer(models.Model):

    id = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, primary_key=True)
    # from the last page of application form
    question1 = models.TextField(blank=True, help_text="Please share with us any academic or extracurricular \
                                                activities, interests, or hobbies you are involved in or enjoy doing.")
    question2 = models.TextField(blank=True, help_text="What are some of your strengths and weaknesses?")

    question3 = models.TextField(blank=True, help_text="why are you interested in study aboard? What do you hope to \
                                                       gain from this experience?")
    question4 = models.TextField(blank=True, help_text="Describe one of the biggest challenges you had to face and \
                                                       what did your learn from this experience?")
    question5 = models.TextField(blank=True, help_text="Describe one person you admire and tell us why you admire \
                                                       him/her?")
    question6 = models.TextField(blank=True, help_text="where do you see yourself when you turn 21?")

    question7 = models.TextField(blank=True, help_text="Write a brief self-introduction for your future host-family.")
