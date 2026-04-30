from urllib.parse import urlparse
from django.conf import settings
from django.db import models
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        if type(view.url_name) == type(None):
            next_url = reverse(index, args=view.args, kwargs=view.kwargs)
        else:
            next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)

        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response


def index(request):
    from .models import Slider, News, Partner
    sliders = Slider.objects.filter(is_active=True).prefetch_related('features', 'modal_items').all()
    latest_news = News.objects.filter(is_published=True, category__slug='yangiliklar').select_related('category').order_by('-published_date')[:9]
    latest_analytics = News.objects.filter(is_published=True, category__slug='tahliliy-materiallar').select_related('category').order_by('-published_date')[:5]
    partners = Partner.objects.all()
    return render(request, 'index.html', {'sliders': sliders, 'latest_news': latest_news, 'latest_analytics': latest_analytics, 'partners': partners})

def admission_page(request):
    return render(request, 'admission-page.html')

def bussines(request):
    return render(request, 'bussines.html')

def department_details(request):
    return render(request, 'department-details.html')

def discounts_page(request):
    from .models import Degree
    degrees = Degree.objects.prefetch_related('program_set').all()
    return render(request, 'discounts-page.html', {'degrees': degrees})

def faq(request):
    from .models import FAQCategory
    categories = FAQCategory.objects.prefetch_related('faqs').all()
    return render(request, 'faq.html', {'categories': categories})

def infrastructure(request):
    from .models import CampusGallery
    galleries = CampusGallery.objects.all()
    return render(request, 'infrastructure.html', {'campus_galleries': galleries})

def internships(request):
    from .models import Partner
    partners = Partner.objects.all()
    return render(request, 'internships.html', {'partners': partners})

def leadership(request):
    from .models import Leader, Department
    leaders = Leader.objects.prefetch_related('experiences').all()
    departments = Department.objects.prefetch_related('employees').all()
    
    kafedralar = departments.filter(type='kafedra')
    bolimlar = departments.filter(type='bolim')
    
    return render(request, 'leadership.html', {
        'leaders': leaders,
        'kafedralar': kafedralar,
        'bolimlar': bolimlar,
    })

def legal(request):
    return render(request, 'legal.html')

def masters(request):
    return render(request, 'masters.html')

def news(request):
    from .models import News
    from django.core.paginator import Paginator
    news_qs = News.objects.filter(is_published=True, category__slug='yangiliklar').order_by('-published_date', '-id')
    paginator = Paginator(news_qs, 18)
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)
    return render(request, 'news.html', {'news_list': news_list})

def analytics(request):
    from .models import News
    from django.core.paginator import Paginator
    analytics_qs = News.objects.filter(is_published=True, category__slug='tahliliy-materiallar').order_by('-published_date', '-id')
    paginator = Paginator(analytics_qs, 18)
    page_number = request.GET.get('page')
    analytics_list = paginator.get_page(page_number)
    return render(request, 'analytics.html', {'analytics_list': analytics_list})
def news_detail(request, slug):
    from .models import News
    article = get_object_or_404(News, slug=slug, is_published=True)
    # Ko'rishlar sonini oshirish
    article.views_count += 1
    article.save(update_fields=['views_count'])
    
    # O'xshash yangiliklar (shu kategoriyadan)
    related_news = News.objects.filter(
        is_published=True, category=article.category
    ).exclude(id=article.id).order_by('-published_date')[:3]
    
    # So'nggi yangiliklar/materiallar (shu kategoriyadan)
    latest_news = News.objects.filter(
        is_published=True, category=article.category
    ).exclude(id=article.id).order_by('-published_date')[:3]
    
    # Top yangiliklar/materiallar (shu kategoriyadan)
    top_news = News.objects.filter(
        is_published=True, category=article.category
    ).exclude(id=article.id).order_by('-views_count')[:3]
    
    return render(request, 'news_detail.html', {
        'article': article,
        'related_news': related_news,
        'latest_news': latest_news,
        'top_news': top_news,
    })

def research(request):
    from .models import Researcher
    researchers = Researcher.objects.all()
    return render(request, 'research.html', {'researchers': researchers})

def resources(request):
    return render(request, 'resources.html')

def rules(request):
    return render(request, 'rules.html')

def shop(request):
    from .models import ShopCategory, ShopProduct
    categories = ShopCategory.objects.annotate(
        product_count=models.Count('products', filter=models.Q(products__is_active=True))
    ).all()
    products = ShopProduct.objects.filter(is_active=True).select_related('category').prefetch_related('colors', 'sizes')
    total_count = products.count()
    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'total_count': total_count,
    })

import json
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def shop_checkout_api(request):
    from .models import ShopOrder, ShopOrderItem, ShopProduct
    try:
        data = json.loads(request.body)
        full_name = data.get('full_name')
        phone = data.get('phone')
        address = data.get('address', '')
        items = data.get('items', [])
        
        if not full_name or not phone or not items:
            return JsonResponse({'status': 'error', 'message': "Iltimos, ismingiz, raqamingiz va mahsulotlarni kiriting!"}, status=400)
        
        total_price = 0
        order = ShopOrder.objects.create(
            full_name=full_name,
            phone=phone,
            address=address,
            total_price=0
        )
        
        for item in items:
            try:
                product = ShopProduct.objects.get(id=item['product_id'])
                quantity = int(item.get('quantity', 1))
                price = product.price
                total_price += price * quantity
                
                ShopOrderItem.objects.create(
                    order=order,
                    product=product,
                    product_name=product.title,
                    color=item.get('color', ''),
                    size=item.get('size', ''),
                    quantity=quantity,
                    price=price
                )
            except ShopProduct.DoesNotExist:
                continue
                
        order.total_price = total_price
        order.save()
        
        return JsonResponse({'status': 'success', 'message': "Buyurtma qabul qilindi!"})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def student_union(request):
    from .models import CouncilMember
    members = CouncilMember.objects.all()
    return render(request, 'student-union.html', {'council_members': members})

def why_team(request):
    return render(request, 'why-team.html')

from django.shortcuts import get_object_or_404
from .models import Program, ProgramApproach

def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)
    approaches = ProgramApproach.objects.all()
    
    # Template tanlash: Bakalavr bo'lsa bussines.html, Magistr bo'lsa masters.html
    # Degree nomini (title_uz) tekshiramiz
    degree_name = program.degree.title_uz.lower()
    
    template_name = 'bussines.html'
    if 'magistr' in degree_name:
        template_name = 'masters.html'
        
    return render(request, template_name, {'program': program, 'approaches': approaches})


# =========================================
# PROGRAM APPLICATION API
# =========================================

@csrf_exempt
def program_application_submit(request):
    """Yo'nalish sahifasidan ariza qabul qilish (Call center uchun)"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST kerak'}, status=405)

    import json
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': "JSON formati noto'g'ri"}, status=400)

    first_name = data.get('first_name', '').strip()
    last_name = data.get('last_name', '').strip()
    middle_name = data.get('middle_name', '').strip()
    phone = data.get('phone', '').strip()
    program_id = data.get('program_id')

    if not first_name or not last_name or not phone:
        return JsonResponse({'error': 'Ism, familiya va telefon majburiy'}, status=400)

    from .models import ProgramApplication

    program = None
    if program_id:
        try:
            program = Program.objects.get(pk=program_id)
        except Program.DoesNotExist:
            pass

    ProgramApplication.objects.create(
        program=program,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name or None,
        phone=phone,
    )

    return JsonResponse({'success': True})


# =========================================
# CHAT API ENDPOINTS
# =========================================

@csrf_exempt
def chat_start(request):
    """Yangi chat suhbatini boshlash"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST kerak'}, status=405)

    import json
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON formati noto\'g\'ri'}, status=400)

    fullname = data.get('fullname', '').strip()
    phone = data.get('phone', '').strip()
    email = data.get('email', '').strip()
    message = data.get('message', '').strip()

    if not fullname or not phone or not message:
        return JsonResponse({'error': 'Ism, telefon va xabar majburiy'}, status=400)

    from .models import ChatConversation, ChatMessage

    conversation = ChatConversation.objects.create(
        fullname=fullname,
        phone=phone,
        email=email or None
    )

    ChatMessage.objects.create(
        conversation=conversation,
        text=message,
        is_from_admin=False
    )

    return JsonResponse({
        'success': True,
        'session_key': str(conversation.session_key),
        'conversation_id': conversation.id
    })


@csrf_exempt
def chat_send(request):
    """Mavjud suhbatga xabar yuborish"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST kerak'}, status=405)

    import json
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON formati noto\'g\'ri'}, status=400)

    session_key = data.get('session_key', '')
    message = data.get('message', '').strip()

    if not session_key or not message:
        return JsonResponse({'error': 'session_key va xabar majburiy'}, status=400)

    from .models import ChatConversation, ChatMessage

    try:
        conversation = ChatConversation.objects.get(session_key=session_key)
    except ChatConversation.DoesNotExist:
        return JsonResponse({'error': 'Suhbat topilmadi'}, status=404)

    ChatMessage.objects.create(
        conversation=conversation,
        text=message,
        is_from_admin=False
    )

    conversation.save()  # updated_at yangilanishi uchun

    return JsonResponse({'success': True})


@csrf_exempt
def chat_messages(request):
    """Suhbat xabarlarini olish (polling)"""
    session_key = request.GET.get('session_key', '')

    if not session_key:
        return JsonResponse({'error': 'session_key majburiy'}, status=400)

    from .models import ChatConversation, ChatMessage

    try:
        conversation = ChatConversation.objects.get(session_key=session_key)
    except ChatConversation.DoesNotExist:
        return JsonResponse({'error': 'Suhbat topilmadi'}, status=404)

    # Admin xabarlarini o'qilgan deb belgilash (foydalanuvchi ko'rdi)
    ChatMessage.objects.filter(
        conversation=conversation,
        is_from_admin=True,
        is_read=False
    ).update(is_read=True)

    messages = conversation.messages.all().values(
        'id', 'text', 'is_from_admin', 'created_at'
    )

    return JsonResponse({
        'success': True,
        'messages': list(messages)
    })


@csrf_exempt
def chat_admin_reply(request):
    """Admin tomonidan javob yuborish"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST kerak'}, status=405)

    # Faqat admin/staff foydalanuvchilar uchun
    if not request.user.is_authenticated or not request.user.is_staff:
        return JsonResponse({'error': 'Ruxsat yo\'q'}, status=403)

    import json
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON noto\'g\'ri'}, status=400)

    conversation_id = data.get('conversation_id')
    message = data.get('message', '').strip()

    if not conversation_id or not message:
        return JsonResponse({'error': 'conversation_id va xabar majburiy'}, status=400)

    from .models import ChatConversation, ChatMessage

    try:
        conversation = ChatConversation.objects.get(pk=conversation_id)
    except ChatConversation.DoesNotExist:
        return JsonResponse({'error': 'Suhbat topilmadi'}, status=404)

    ChatMessage.objects.create(
        conversation=conversation,
        text=message,
        is_from_admin=True,
        is_read=False
    )

    conversation.save()  # updated_at yangilanishi uchun

    return JsonResponse({'success': True})
