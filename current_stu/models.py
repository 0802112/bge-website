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

    test = models.TextField(blank=True)

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    englishname = models.CharField(max_length=30)
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
    id = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    marital = models.CharField(max_length=10, choices=MARITAL_STATUS, default='MARRIED',)
    occupation = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    day_phone = models.CharField(max_length=20)
    email = models.EmailField()


class MotherInfo(models.Model):
    id = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    marital = models.CharField(max_length=10, choices=MARITAL_STATUS, default='MARRIED',)
    occupation = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    day_phone = models.CharField(max_length=20)
    email = models.EmailField()


class ContactInfo(models.Model):
    id = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, primary_key=True)

    CONTACT_TIME = (
        ('MORNING', 'Mornings'),
        ('AFTERNOON', 'Afternoons'),
        ('EVENING', 'Evenings'),
        ('WEEKDAY', 'Weekdays'),
        ('WEEKEND', 'Weekends'),
    )

    address = models.CharField(max_length=200)
    apt = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    home_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField()


class AdditionalHousehold(models.Model):

    name1 = models.CharField(max_length=50)
    gender1 = models.CharField(max_length=6)
    relationship1 = models.CharField(max_length=10)
    school1 = models.CharField(max_length=50)
    age1 = models.IntegerField(max_length=3)
    grade1 = models.CharField(max_length=50)

    name2 = models.CharField(max_length=50)
    gender2 = models.CharField(max_length=6)
    relationship2 = models.CharField(max_length=10)
    school2 = models.CharField(max_length=50)
    age2 = models.IntegerField(max_length=3)
    grade2 = models.CharField(max_length=50)

    name3 = models.CharField(max_length=50)
    gender3 = models.CharField(max_length=6)
    relationship3 = models.CharField(max_length=10)
    school3 = models.CharField(max_length=50)
    age3 = models.IntegerField(max_length=3)
    grade3 = models.CharField(max_length=50)


class SchoolInfo(models.Model):

    currentschool = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    grade = models.IntegerField(max_length=2)
    gpa = models.CharField(max_length=3)
    rank = models.CharField(max_length=50)
    enrolldate = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    post = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField()


class TestScore(models.Model):
    slep = models.IntegerField()
    slepdate = models.CharField(max_length=20)
    toefl = models.IntegerField()
    toefldate = models.CharField(max_length=20)
    ssat = models.IntegerField()
    ssatdate = models.CharField(max_length=20)
    sat = models.IntegerField()
    satdate = models.CharField(max_length=20)
    act = models.IntegerField()
    actdate = models.CharField(max_length=20)
    other = models.IntegerField()
    otherdate = models.CharField(max_length=20)


class History(models.Model):

    visit = models.CharField(max_length=3)
    when = models.CharField(max_length=255)
    long = models.CharField(max_length=50)
    reason = models.CharField(max_length=255)
    rate = models.CharField(max_length=50)


class Profile(models.Model):

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

    id = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, primary_key=True)

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
    personality = models.CharField(max_length=20, choices=PERSONALITY, blank=True, null=True)

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
    eat = models.CharField(max_length=30, choices=EAT, blank=True, null=True)

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
    not_eat = models.CharField(max_length=30, choices=NOT_EAT, blank=True, null=True)

    SPECIAL_DIET = (
        ('DAIRY', 'Dairy_Free'),
        ('GLUTEN', 'Gluten_Free'),
        ('VEGETARIAN', 'Vegetarian'),
        ('VEGAN', 'Vegan'),
        ('OR', 'Other')
    )
    special_diet = models.CharField(max_length=20, choices=SPECIAL_DIET, blank=True, null=True)

    ALLERGY = (
        ('NUTS', 'Nuts'),
        ('MILK', 'Milk'),
        ('FISH', 'Fish'),
        ('VEGAN', 'Vegan'),
        ('WHEAT', 'Wheat'),
        ('OR', 'Other')
    )
    allergy = models.CharField(max_length=20, choices=ALLERGY, blank=True, null=True)

    RESTAURANT = (
        ('CH', 'Chinese'),
        ('KR', 'Korean'),
        ('JP', 'Japanese'),
        ('US', 'American'),
        ('MN', 'Mexican'),
        ('IY', 'Italian'),
        ('OR', 'Other')
    )
    restaurant = models.CharField(max_length=2, choices=RESTAURANT, blank=True, null=True)

    OWN_MEAL = (
        ('YES', 'Yes'),
        ('NO', 'No')
    )
    own_meal = models.CharField(max_length=3, choices=OWN_MEAL, blank=True, null=True)

    ##############
    # Preferences
    PET = (
        ('CAT', 'Like cats'),
        ('DOG', 'Like dogs'),
        ('ALL', 'Like all animals'),
        ('NO', "Don't like animals")
    )
    pet = models.CharField(max_length=3, choices=PET, blank=True, null=True)

    SMOKE = (
        ('YES', 'yes'),
        ('NO', 'no')
    )
    smoke = models.CharField(max_length=3, choices=SMOKE, blank=True, null=True)

    SMOKE_FREE = (
        ('YES', 'yes'),
        ('NO', 'no')
    )
    smoke_free = models.CharField(max_length=3, choices=SMOKE_FREE, blank=True, null=True)

    RElIGIOUS_SERVICE = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('DCARE', "Don't care")
    )
    religious_service = models.CharField(max_length=5, choices=RElIGIOUS_SERVICE, blank=True, null=True)

    WEEKDAY_CURFEW = (
        ('9', '9PM'),
        ('10', '10PM'),
        ('11', '11PM'),
        ('12', '12MM')
    )
    weekday_curfew = models.CharField(max_length=2, choices=WEEKDAY_CURFEW, blank=True, null=True)

    WEEKEND_CURFEW = (
        ('11', '11PM'),
        ('12', '12AM'),
        ('1', '1AM'),
        ('2', '2AM')
    )
    weekend_curfew = models.CharField(max_length=2, choices=WEEKEND_CURFEW, blank=True, null=True)


#######################################################################################


class ShortAnswer(models.Model):

    id = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, primary_key=True)
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
