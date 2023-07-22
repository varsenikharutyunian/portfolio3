from django.contrib import admin
from .models import  Skill, Education,Experience,Language,Courses,Service


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date", "end_date", "grade", "created_on"]
    list_filter = ["start_date"]


class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]
    list_filter = ["value"]
    search_fields = ["name"]

class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name","level"]
    
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["position_name", "start_date",
                    "end_date", "company_name", "created_on"]
    list_filter = ["start_date"]

class CoursesAdmin(admin.ModelAdmin):
    list_display = ["position_name", "start_date",
                    "end_date", "company_name", "created_on"]
    list_filter = ["start_date"]

# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ["name", "job_position","opinion","image","created_on"]
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position')

class ServicekAdmin(admin.ModelAdmin):
    list_display = ["service_name", "service_description"]




# Register your models here.
admin.site.register(Skill,SkillAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Language,LanguageAdmin)
# admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(Service, ServicekAdmin)
admin.site.register(Courses)




