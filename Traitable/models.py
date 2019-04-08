from django.db import models
from django.conf import settings
from django.utils import timezone
import csv
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# some validator declarations that I use within the Pub & Trait models
val_alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Error: only alphanumeric characters are allowed.')
val_alpha = RegexValidator(r'^[a-zA-Z]*$', 'Error: only alphabetic characters are allowed.')
val_numeric = RegexValidator(r'^[0-9]*$', 'Error: only numeric characters are allowed.')
# add in hyphens to names

# Pub model below; all Pub-related variables declared within it
class Pub(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Publication name')
    lastName = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha], verbose_name = "Author's last name")
    middleName = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha], verbose_name = "Author's middle name")
    firstName = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha], verbose_name = "Author's first name")
    citekey = models.CharField(max_length=50, unique=True, null=True, validators=[val_alphanumeric]) #null=True, blank=False
    
    # for variables with multiple options, must define said options on one line (in pairs, as below) and the variable on separate line
    PUB_TYPE_CHOICES = (('article', 'article'), ('book','book'))
    pub_type = models.CharField(max_length=50, null=True, blank=True, choices=PUB_TYPE_CHOICES)

    class Meta:
        #Gives the proper plural name for admin
        verbose_name_plural = "Pubs"

    def __unicode__(self):
        return self.citekey

    def __str__(self):
        return self.citekey

# Trait model below; all Trait-related variables declared within it
class Trait(models.Model):
   # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_reference = models.ForeignKey(Pub, blank=True, null=True, on_delete=models.PROTECT, verbose_name='citekey', validators=[val_alphanumeric])
    genus = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha])#help_text= 'Enter data if known. Expects str as input')
    species = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha])
    isi = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0, message='Must be a number between 0.0 and 1.0'), MaxValueValidator(1.0, message='Must be a number between 0.0 and 1.0')], verbose_name='Index of Self-Incompatibility')
    
    FRUIT_TYPE_CHOICES = (('capsule','capsule'), ('CAPSULE', 'CAPSULE'), ('Capsule', 'Capsule'),('berry','berry'), ('Berry', 'Berry'), ('BERRY', 'BERRY')) # check why need doubles 
    fruit_type = models.CharField(max_length=50, null=True, blank=True, default='none', choices=FRUIT_TYPE_CHOICES)

    #the following 2 variables will show on admin page a date/time stamp when a Trait was added to the database.
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Traits"

    def __unicode__(self):
        return self.pub_reference

    def __str__(self):
        return (str(self.genus)+' '+str(self.species))