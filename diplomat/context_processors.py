from .models import Degree

def degrees_processor(request):
    """
    Kategoriyalar (darajalar) va ularga tegishli yo'nalishlarni hamma sahifada ishlatish uchun.
    Bu menyuni dinamik qiladi.
    """
    degrees = Degree.objects.prefetch_related('program_set').all()
    return {
        'menu_degrees': degrees
    }
