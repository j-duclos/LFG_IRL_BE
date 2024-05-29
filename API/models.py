from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
]

INTEREST_CHOICES = [
    ("BG", "Board Games"),
    ("VG", "Video Games"),
    ("SP", "Sports"),
    ("DI", "Dinner"),
    ("HO", "Hang out"),
]

DISTANCE_CHOICES = [
    (5, "5 miles"),
    (10, "10 miles"),
    (20, "20 miles"),
    (40, "40 miles"),
    (75, "75 miles"),
    (100, "100 miles"),
]

SCHEDULE_CHOICES = [
    ("WE", "Weekends"),
    ("WD", "Weekdays"),
    ("WN", "Weeknights"),
    ("DA", "Days"),
    ("NI", "Nights"),
    ("AT", "Anytime"),
]

PLATFORM_CHOICES = [
    ("XB", "Xbox"),
    ("PS", "PS"),
    ("PC", "PC"),
    ("NT", "Nintendo"),
    ("OT", "Other"),
    ("NO", "None"),
]

class Interest(models.Model):
    name = models.CharField(max_length=50, choices=INTEREST_CHOICES)

    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    free = models.CharField(max_length=20, choices=SCHEDULE_CHOICES)

    def __str__(self):
        return self.free

class Platform(models.Model):
	name = models.CharField(max_length=20, choices=PLATFORM_CHOICES)

	def __str__(self):
		return self.name

""" class Gender(models.Model):
     name = models.CharField(max_length=1, choices=GENDER_CHOICES)

     def __str__(self):
          return self.name """

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    gamer_tag = models.CharField(max_length=50, blank=False, null=False)
    display_gamer_tag = models.BooleanField(default=True)
    age = models.IntegerField(blank=False, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    zip = models.IntegerField(blank=False, null=False)
    bio = models.TextField()
    radius = models.IntegerField(choices=DISTANCE_CHOICES, default=20)
    interest = models.ManyToManyField(Interest, related_name='profiles')
    schedule = models.ManyToManyField(Schedule, related_name='profiles')
    platform = models.ManyToManyField(Platform, related_name='profiles')
    #interest = models.ManyToManyField(max_length=2, choices=INTEREST_CHOICES, default="HO")
    #schedule = models.ManyToManyField(max_length=2, choices=SCHEDULE_CHOICES, default="AT")
    #platform = models.ManyToManyField(max_length=2, choices=PLATFORM_CHOICES, default="NO")
    coin_balance = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    #pic1 = models.ImageField(blank=True, width_field=120, height_field=120)
    #radius = models.IntegerField(choices=DISTANCE_CHOICES, default=20)
    #interest = models.ManyToManyField(max_length=2, choices=INTEREST_CHOICES)
    #currLevel = models.IntegerField(blank=False, null=False, default=1)
    #xpPoints = models.IntegerField(blank=False, null=False)
    #schedule = models.ManyToManyField(max_length=2, choices=SCHEDULE_CHOICES)
    #platform = models.ManyToManyField(max_length=2, choices=PLATFORM_CHOICES)
    
    def __str__(self):
        return self.username
    
    def add_credit(self, amount):
        self.coin_balance += amount
        return f'Your new balance is: {self.coin_balance}'

    def spend_credit(self, amount):
        self.coin_balance -= amount
        return f'Your new balance is {self.coin_balance}'


""" class CommonInfo(models.Model):
	title = models.CharField(max_length=75)
	pLeader = models.ForeignKey(User, on_delete=models.CASCADE)
	#interest = models.CharField(max_length=30, choices=INTEREST_CHOICES)
	#meetupTime = models.DateTimeField()
	currentPartyCount = models.IntegerField()
	neededPartyCount = models.IntegerField()
	locationCity = models.CharField(max_length=50)
	locationState = models.CharField(max_length=25)
	locationZip = models.CharField(max_length=7)
	partySpecifics = models.TextField()

	class Meta:
		abstract = True """

#class LFGAlert(CommonInfo):
class LFGAlert(models.Model):
    """ fill out """

    title = models.CharField(max_length=75)
    #meetupAddress = models.TextField()
    #invitesSent = models.IntegerField()

    #invitesAccepted = models.IntegerField()
    #invitesDeclined = models.IntegerField()
    #inviteDetails = models.CharField()





""" class Invite(CommonInfo):
	
    #invitedUser = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=25) """
     








class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title