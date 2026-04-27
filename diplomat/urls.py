from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admission-page/', views.admission_page, name='admission_page'),
    path('bussines/', views.bussines, name='bussines'),
    path('department-details/', views.department_details, name='department_details'),
    path('discounts-page/', views.discounts_page, name='discounts_page'),
    path('faq/', views.faq, name='faq'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('internships/', views.internships, name='internships'),
    path('leadership/', views.leadership, name='leadership'),
    path('legal/', views.legal, name='legal'),
    path('masters/', views.masters, name='masters'),
    path('news/', views.news, name='news'),
    path('analytics/', views.analytics, name='analytics'),
    path('research/', views.research, name='research'),
    path('resources/', views.resources, name='resources'),
    path('rules/', views.rules, name='rules'),
    path('shop/', views.shop, name='shop'),
    path('shop/checkout/', views.shop_checkout_api, name='shop_checkout_api'),
    path('student-union/', views.student_union, name='student_union'),
    path('why-team/', views.why_team, name='why_team'),
    path('admission/<slug:slug>/', views.program_detail, name='program_detail'),
]

