from django.http import HttpResponse
from django.shortcuts import render
from xhtml2pdf import pisa
from cvg.models import CvProfile
from django.template import loader
from weasyprint import HTML, CSS
import io


# Create your views here.
def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        summary = request.POST.get('summary')
        skills = request.POST.get('skills')
        experience = request.POST.get('experience')
        education = request.POST.get('education')
        personal_info = request.POST.get('personal_info')
        work_experience = request.POST.get('work_experience')
        previous_employment = request.POST.get('previous_employment')
        certifications = request.POST.get('certifications')
        references = request.POST.get('references')
        contact_info = request.POST.get('contact_info')
        other_skills = request.POST.get('other_skills')
        interests = request.POST.get('interests')
        projects = request.POST.get('projects')

        cv_profile, created = CvProfile.objects.get_or_create(name=name, email=email, mobile=mobile, summary=summary,
                                                     skills=skills,
                                                     experience=experience,
                                                     education=education, projects=projects, interests=interests,
                                                     personal_info=personal_info,
                                                     work_experience=work_experience,
                                                     previous_employment=previous_employment,
                                                     certifications=certifications, references=references,
                                                     contact_info=contact_info,
                                                     other_skills=other_skills)
        if not created:
            cv_profile.save()
    return render(request, 'cvg/accept.html')


def resume(request, id):
    options = {
        'page-size': 'Letter',
        'ecoding': 'utf-8'
    }
    user = CvProfile.objects.get(pk=id)
    template = loader.get_template('cvg/resume.html')
    html = template.render({'user': user})
    pdf = HTML(string=html).write_pdf(**options, stylesheets=[CSS('./static/cvg/resume.css')])

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response
