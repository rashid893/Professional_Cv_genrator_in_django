from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Profile,Contact

# Register your models here.
@admin.register(Profile)
class StudentAdmin(admin.ModelAdmin):
 list_display=['id', 'name','jobtitle', 'email','gitlink','linkd','number','profile','skill1','skill2','skill3','technichal1','technichal2','technichal3','technichal4','technichal5','companyname','sdate','edate','uname','dptname','cgpa','profile_image']

@admin.register(Contact)
class ConactAdmin(admin.ModelAdmin):
 list_display=['id','name','subject','email','message']


                                                                                                                                                                              