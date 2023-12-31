from django.shortcuts import render, HttpResponse
from .models import Vacancy, Company

# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse('Найдите работу или работника мечты!')

def contact_view(request):
    return HttpResponse('''
        <div>
            Phone: +3874628734 <br>
            Email: kaium@gmail.com
        </div>
    ''')

def address(request):
    return HttpResponse('''
        <ul>
            <li>г. Бишкек, 7 м-н, 26/1</li>
            <li>г. Ош, Черёмушка, дом 235</li>
        </ul>
    ''')


def vacancy_list(request):
    vacancies = Vacancy.objects.all()  # в Django ORM "SELECT * FROM Vacancies"
    context = {"vacancies": vacancies}  # context data для jinja2
    context["example"] = "hello"
    return render(request, 'vacancies.html', context)

def company(request):
    companys=Company.objects.all() #SElect в Django ORM
    context={"companys":companys}
    return render(request, 'companys.html',context)

def vacancy_info(request, id):
    candidates = vacancy_objects.candidate.all()
    vacancy_object = Vacancy.objects.get(id=id)
    return render(
        request, 'vacancies_detail.html',
        {'vacancy': vacancy_object}, candidates
    )
