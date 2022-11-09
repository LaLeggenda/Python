#from bs4 import BeautifulSoup
#soup = BeautifulSoup("lalalalalal", "html.parser")
#ciao
class Job:
  def __init__(self, title, company, description, skills, location):
    self.company = company
    self.title = title
    self.description = description
    self.skills = skills
    self.location = location
    self.recruiter = Recruiter

class Person:
  def __init__(self, age, address, cell, first_name, last_name, catch_phrase):
    self.age = age
    self.address = address
    self.cell = cell
    self. first_name = first_name
    self.last_name = last_name
    self.catch_phrase = catch_phrase
    
  def Personal_Details(self):
    details = f"""
    Name: {self.first_name}
    Surname: {self.last_name}
    Age: {self.age}
    Address:{self.address}
    Cellular:{self.cell}\n"""
    return details

class Candidate(Person):
  def __init__(self, age, address, cell, first_name, last_name, catch_phrase, degree, salary, notice_time, skills):
    super().__init__(age,address, cell, first_name, last_name, catch_phrase)
    self.degree = degree
    self.salary = salary
    self.notice_time = notice_time
    self. skills = skills
  def Application(self):
    print("Applied...");

class Recruiter(Person):
  def __init__(self, age, address, cell, first_name, last_name, catch_phrase, Job):
    super().__init__(age,address, cell, first_name, last_name, catch_phrase)
    self.Job=Job
  def jobposting(self):
    details = f"""
    Recruiter: {self.first_name +" "+ self.last_name }
    Company: {self.Job.company}
    Title: {self.Job.title}
    Description: {self.Job.description}
    Skills: {self.Job.skills}
    Location:{self.Job.location}\n"""
    return details


User = Person(25, "Via Emilia 80, Bologna", "+393334592351", "Ciceruacchio", "Altobelli","you know nothing, Jon Snow")
User2 = Candidate(25, "Via Emilia 80, Bologna", "+393334592351", "Ciceruacchio", "Altobelli","you know nothing, Jon Snow", "Engineering" ,"30000" ,"2 months" ,"quasi un tecnico")

Job1 = Job("Project Manager", "CNH", "coordinator of activities","na cos a piacer", "Modena")
Job2 = Job("Riggiularo", "Sassuolo riggiole snc", "coordinator of riggiole","riggiole cutting", "Sassuolo")
Job3 = Job("Software Engineer", "Ferrari", "code writer","C,C++", "Maranello")

User3 = Recruiter(25, "Via Emilia 80, Bologna", "+393334592351", "Carmelina", "Lestofanti","you know nothing, Jon Snow", Job1)

print(User.catch_phrase);
print(User.Personal_Details());
print(User2.degree);
User2.Application();
print(User3.Job.company);
print(User3.jobposting());
listJobs= [];
listJobs.append(Job1);
listJobs.append(Job2);
listJobs.append(Job3);

for obj in listJobs:
  print(obj.title, sep=' ')
