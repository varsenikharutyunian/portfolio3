from django.shortcuts import render
# from django.http import HttpResponse
from .models import (Skill,Education,Language,Courses,Experience,Service,PersonalInfo)
from .forms import MessageForm

# Create your views here.
def portfolio(request):
    return render(request,"portfolio.html",
                    context={"name":"VARSENIK",
                            "surename":"HARUTYUNYAN",
                            "phone":"+37493912442",
                            "email":"varsikharutyunyan72@gmail.com",
                            "social1":"facebook.com",
                            "social2":"instagran.com",
                            "language1":"Armenian (native)",
                            "language2":"Russian",
                            "language3":"English",
                            "language4":"Franse",
                            "skills1":"Linux",
                            "skills2":"HTML/CSS",
                            "skills3":"Python",
                            "skills4":"Django",
                            "Skills1":"Teaching ability",
                            "Skills2":"Team working",
                            "Skills3":"Analytical thinking",
                            "Skills4":"Mathematical thinking",
                            "Skills5":"Proper management of time",
                            
                            "about_me":"""Hello. I am a teacher.ince 1993, I have been working as a physics and mathematics teacher.I live in Bazmaghbyur village.Now I'm learning Python programming.I am married, I have a daughter and a son.""",         
                            
                            "education1":"1990-1996, Armenian State University of Engineering Radio Engineering Department",
                            "education2":"2005-2008, Armenian State Pedagogical University AF. KH. Abovyan.",
                            "experience":[
                                {"jobe_title":"teacher","company":"Shcools","period":"1993-Courent"},
                                {"jobe_title":"Python junior developer","company":"XYZ", "period":"2023-Courent"},
                            ]})





def home(request):
    
    status = 200

    if request.method == "POST":
        print("POSTED DATA")
        print(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            status = 201
        else:
            print("TELL them that sent data is not valid")
    
    
    skills=Skill.objects.filter(user__username= "varsik")
    education = Education.objects.all()
    experience = Experience.objects.all()
    language = Language.objects.all()
    courses = Courses.objects.all()
    services = Service.objects.all()
    # testimonials = Testimonials.objects.all()
    personal_info = PersonalInfo.objects.get(user__username = "varsik")
    messageForm = MessageForm()
    
    
    data={
        # "first_name":"VARSENIK",
        # "last_name":"HARUTYUNYAN",
        # "address": "RA, Bazmaghbyur avenue 3/5",
        # "phone": "+37493912442",
        # "web": "varsikharutyunyan.pythonanywhere.com",
        # "email":"varsikharutyunyan72@gmail.com",
        # "age": "50",
        # "birthday": "02 Nov 1972",
        # 'city': "Ashtarak,Bazmaghbyur, RA",
        # "title": "Portfolio Varsenik Harutyunyan",
        # "degree": "Junior",
        
                                            
        # 'linkdin': 'https://www.linkedin.com/in/avagyani',
        # 'skype': 'https://join.skype.com/invite/M0yS4sB2gOvL',
        "facebook": "https://www.facebook.com/varsenik.harutunyan",
        "instagram": "https://www.instagram.com/varsenikharutunyan/",
        "text1":"Hello! It's wonderful to hear about your teaching experience as a physics and mathematics teacher since 1993 in Bazmaghbyur village. Congratulations on starting your journey in learning Python programming. Python is a versatile and popular programming language, and I'm sure it will open up new possibilities for you.",
        "text2": "I am a beginner Python programmer.",
        'text3': "Now I am learning Python within the AGBU .",
        'text4': "I passed first level (Introduction to Python) and started learning advanced course (Web development).",                                                "skills":skills,
        "courses": courses,
        "education": education,
        "experience": experience,
        "language": language, 
        "services": services,
        # "testimonials": testimonials,
        "personal_info":personal_info,
        "messageForm": messageForm,
        }
    
    return render(request,"index.html",context=data,status=status)