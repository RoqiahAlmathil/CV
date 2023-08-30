fvclass Experience:
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date
        
    def display_experience(self):
        print(f"company:{self.company}")
        print(f"job_title:{self.job_title}")
        print(f"start_date:{self.start_date}")
        print(f"end_date:{self.end_date}")

class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date
        
    def display_education(self):
        print(f"degree:{self.degree}")
        print(f"institution:{self.institution}")
        print(f"Date:{self.completion_date}")
     

class Skill:
    def __init__(self, skill,percentage):
        self.skill = skill
        self.percentage = percentage

    def display_skill(self):
        print(f"skill:{self.skill}")
        print(f"percentage:{self.percentage}")
        
class CV:
    def __init__(self):
        self.experience = []
        self.education = []
        self.skill = []
        
    def add_experience(self):
        company=input("Enter the company name:")
        job_title=input("Enter the job_title name:")
        start_date=input("Enter the start_date name:")
        end_date=input("Enter the end_date name:")
        experience=Experience(company, job_title, start_date, end_date)
        self.experience.append(experience)
        add_more=input("DO you want to add anothor experience?(yes/no):")
        if add_more.lower()=="yes":
            self.add_experience()
            
    def add_education(self):
        degree=input("Enter the degree :")
        institution=input("Enter the institution :")
        completion_date=input("Enter the completion_date:")
        education=Education(degree, institution, completion_date)
        self.education.append(education)
        add_more=input("DO you want to add anothor education?(yes/no):")
        if add_more.lower()=="yes":
            self.add_education()
            
    def add_skill(self):
        skill=input("Enter the skill :")
        percentage=input("Enter the percentage :")
        skill=Skill(skill, percentage)
        self.skill.append(skill)
        add_more=input("DO you want to add anothor skill?(yes/no):")
        if add_more.lower()=="yes":
            self.add_skill()
    def display_cv(self):
        print("CV")
        print("--------experience----------")
        for experience in self.experience:
            experience.display_experience()
        print("-------education--------------")
        for education in self.education:
            education.display_education()
        print("----------skill---------------")
        for skill in self.skill:
            skill.display_skill()
        print("-------------------------------------")
        
name = input("Enter your name:") 
cv = CV()
add_skill = input("DO you want to add  skill?(yes/no):")  
if add_skill.lower()=="yes": 
    cv.add_skill() 
add_education = input("DO you want to add  education?(yes/no):")  
if add_education.lower()=="yes": 
    cv.add_education()
add_experience = input("DO you want to add  experience?(yes/no):")  
if add_experience.lower()=="yes":
    cv.add_experience()
cv.display_cv()    
    
            
            
