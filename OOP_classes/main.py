"""Опишіть класи, використовуючи принципи з уроку. Ви повинні реалізувати різні атрибути (мінімум 2 для
батьківського класу) і методи (мінімум 2 для кожного з класів)

For example:

Animals -> mammals -> flying mammals-> Bird -> Eagle
............................
Слід запровадити щонайменше 3 ланцюжки наслідування

Класи мають бути в різних модулях. У вас повинно бути не менше 9 різних класів."""

from colorist import Colorist
from surgeon import Surgeon
from qa import Qa
from hr import Hr

colorist = Colorist("colorist")
coloring_techniques = ["air-touch", "total blond"]
colorist.add_coloring_techniques(coloring_techniques)
colorist.show_coloring_techniques()
service = ["cutting", "coloring", "styling"]
colorist.add_service_list(service)
colorist.show_service_list()
print(colorist.name)
colorist.name = "super colorist"
print(colorist.name)
colorist.add_skills("accuracy")
print(colorist.show_skills())

surgeon = Surgeon("surgeon")
surgeon.change_years_of_operating_activity(10)
print(surgeon.show_years_of_operating_activity())
surgeon.let_access_to_operations_as_primary_surgeon()
surgeon.appoint_family_doctor(True)
surgeon.change_age_of_internship(10)
surgeon.change_med_level()
print(surgeon.show_med_level())
print(surgeon.name)
surgeon.name = "heart surgeon"
print(surgeon.name)
surgeon.add_skills("cutting peoples")
print(surgeon.show_skills())

qa = Qa('qa', 10, "upper")
qa.automation = True
qa.add_programming_languages("python")
print(qa.automation, qa.show_programming_languages())
qa.years_experience = 6
qa.english_level = "upper-intermediate"
print(qa.years_experience, qa.english_level)
print(qa.name)
qa.name = "software tester"
print(qa.name)
skills = ["manual tasting", "analitical skills"]
qa.add_skills(skills)
print(qa.show_skills())

hr = Hr('hr', 10, "upper")
hr.change_closed_vacancies(20)
hr.years_experience = 10
hr.english_level = "advanced"
print(hr.years_experience, hr.english_level)
print(hr.name)
hr.name = "researcher"
print(hr.name)
skills = ["researching", "head hunting"]
hr.add_skills(skills)
print(hr.show_skills())
print(qa)
print(hr)
print(surgeon)
print(colorist)

qa.show_expected_salary()
hr.show_expected_salary()
surgeon.show_expected_salary()
colorist.show_expected_salary()