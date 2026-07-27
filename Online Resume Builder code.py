# Online Resume Builder - Combined Project Code

## forms.py

from django import forms

class ResumeForm(forms.Form):

```
full_name = forms.CharField(max_length=100)
phone = forms.CharField(max_length=15)
email = forms.EmailField()
city = forms.CharField(max_length=100)
linkedin = forms.URLField(required=False)

summary = forms.CharField(widget=forms.Textarea)

degree = forms.CharField(max_length=100)
college = forms.CharField(max_length=200)
graduation_year = forms.CharField(max_length=10)
cgpa = forms.CharField(max_length=20, required=False)

company = forms.CharField(max_length=100, required=False)
job_title = forms.CharField(max_length=100, required=False)
employment_dates = forms.CharField(max_length=100, required=False)
responsibilities = forms.CharField(widget=forms.Textarea, required=False)

technical_skills = forms.CharField(widget=forms.Textarea)
software_tools = forms.CharField(widget=forms.Textarea)
soft_skills = forms.CharField(widget=forms.Textarea)

project_title = forms.CharField(max_length=200)
technologies_used = forms.CharField(max_length=200)
project_description = forms.CharField(widget=forms.Textarea)

certifications = forms.CharField(widget=forms.Textarea, required=False)
achievements = forms.CharField(widget=forms.Textarea, required=False)
languages = forms.CharField(widget=forms.Textarea, required=False)
interests = forms.CharField(widget=forms.Textarea, required=False)
```

---

## views.py

from django.shortcuts import render
from .forms import ResumeForm

def home(request):

```
if request.method == 'POST':
    form = ResumeForm(request.POST)

    if form.is_valid():
        return render(request, 'resume.html', form.cleaned_data)

else:
    form = ResumeForm()

return render(request, 'home.html', {'form': form})
```

---

## resume_builder/urls.py

from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
]

---

## resumebuilder/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('resume_builder.urls')),
]

---

## home.html

<!DOCTYPE html>

<html>
<head>
<title>Online Resume Builder</title>
</head>
<body>

<h1>Online Resume Builder</h1>

<form method="POST">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">Generate Resume</button>
</form>

</body>
</html>

---

## resume.html

<!DOCTYPE html>

<html>
<head>
<title>Resume</title>
</head>
<body>

<h1>{{ full_name }}</h1>

<p><b>Phone:</b> {{ phone }}</p>
<p><b>Email:</b> {{ email }}</p>
<p><b>City:</b> {{ city }}</p>
<p><b>LinkedIn:</b> {{ linkedin }}</p>

<h2>Professional Summary</h2>
<p>{{ summary }}</p>

<h2>Education</h2>
<p>{{ degree }}</p>
<p>{{ college }}</p>
<p>{{ graduation_year }}</p>
<p>{{ cgpa }}</p>

<h2>Work Experience</h2>
<p>{{ company }}</p>
<p>{{ job_title }}</p>
<p>{{ employment_dates }}</p>
<p>{{ responsibilities }}</p>

<h2>Skills</h2>
<p>{{ technical_skills }}</p>
<p>{{ software_tools }}</p>
<p>{{ soft_skills }}</p>

<h2>Projects</h2>
<p>{{ project_title }}</p>
<p>{{ technologies_used }}</p>
<p>{{ project_description }}</p>

<h2>Certifications</h2>
<p>{{ certifications }}</p>

<h2>Achievements</h2>
<p>{{ achievements }}</p>

<h2>Languages</h2>
<p>{{ languages }}</p>

<h2>Interests</h2>
<p>{{ interests }}</p>

</body>
</html>
