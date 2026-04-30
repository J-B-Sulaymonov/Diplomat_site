from django.db import models

class Degree(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ta'lim darajasi nomi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ta'lim darajasi"
        verbose_name_plural = "Ta'lim darajalari"

class EducationForm(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ta'lim shakli nomi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ta'lim shakli"
        verbose_name_plural = "Ta'lim shakllari"


ICON_CHOICES = [
    ('fab fa-facebook-f', 'fab fa-facebook-f'),
    ('fab fa-instagram', 'fab fa-instagram'),
    ('fab fa-linkedin-in', 'fab fa-linkedin-in'),
    ('fab fa-telegram-plane', 'fab fa-telegram-plane'),
    ('fab fa-youtube', 'fab fa-youtube'),
    ('far fa-calendar-alt', 'far fa-calendar-alt'),
    ('far fa-clock', 'far fa-clock'),
    ('fas fa-arrow-left', 'fas fa-arrow-left'),
    ('fas fa-arrow-right', 'fas fa-arrow-right'),
    ('fas fa-atom', 'fas fa-atom'),
    ('fas fa-award', 'fas fa-award'),
    ('fas fa-balance-scale', 'fas fa-balance-scale'),
    ('fas fa-binoculars', 'fas fa-binoculars'),
    ('fas fa-bolt', 'fas fa-bolt'),
    ('fas fa-book', 'fas fa-book'),
    ('fas fa-book-open', 'fas fa-book-open'),
    ('fas fa-book-reader', 'fas fa-book-reader'),
    ('fas fa-brain', 'fas fa-brain'),
    ('fas fa-briefcase', 'fas fa-briefcase'),
    ('fas fa-building', 'fas fa-building'),
    ('fas fa-bullhorn', 'fas fa-bullhorn'),
    ('fas fa-bullseye', 'fas fa-bullseye'),
    ('fas fa-calculator', 'fas fa-calculator'),
    ('fas fa-calendar-alt', 'fas fa-calendar-alt'),
    ('fas fa-calendar-check', 'fas fa-calendar-check'),
    ('fas fa-certificate', 'fas fa-certificate'),
    ('fas fa-chalkboard', 'fas fa-chalkboard'),
    ('fas fa-chalkboard-teacher', 'fas fa-chalkboard-teacher'),
    ('fas fa-chart-bar', 'fas fa-chart-bar'),
    ('fas fa-chart-line', 'fas fa-chart-line'),
    ('fas fa-chart-pie', 'fas fa-chart-pie'),
    ('fas fa-check', 'fas fa-check'),
    ('fas fa-check-circle', 'fas fa-check-circle'),
    ('fas fa-check-double', 'fas fa-check-double'),
    ('fas fa-chess', 'fas fa-chess'),
    ('fas fa-chess-king', 'fas fa-chess-king'),
    ('fas fa-chess-knight', 'fas fa-chess-knight'),
    ('fas fa-chevron-down', 'fas fa-chevron-down'),
    ('fas fa-chevron-right', 'fas fa-chevron-right'),
    ('fas fa-city', 'fas fa-city'),
    ('fas fa-clipboard-list', 'fas fa-clipboard-list'),
    ('fas fa-clock', 'fas fa-clock'),
    ('fas fa-cloud', 'fas fa-cloud'),
    ('fas fa-code', 'fas fa-code'),
    ('fas fa-coffee', 'fas fa-coffee'),
    ('fas fa-cog', 'fas fa-cog'),
    ('fas fa-cogs', 'fas fa-cogs'),
    ('fas fa-coins', 'fas fa-coins'),
    ('fas fa-comment-dots', 'fas fa-comment-dots'),
    ('fas fa-comments', 'fas fa-comments'),
    ('fas fa-couch', 'fas fa-couch'),
    ('fas fa-crown', 'fas fa-crown'),
    ('fas fa-database', 'fas fa-database'),
    ('fas fa-desktop', 'fas fa-desktop'),
    ('fas fa-dumbbell', 'fas fa-dumbbell'),
    ('fas fa-envelope', 'fas fa-envelope'),
    ('fas fa-exchange-alt', 'fas fa-exchange-alt'),
    ('fas fa-expand-arrows-alt', 'fas fa-expand-arrows-alt'),
    ('fas fa-external-link-alt', 'fas fa-external-link-alt'),
    ('fas fa-eye', 'fas fa-eye'),
    ('fas fa-feather', 'fas fa-feather'),
    ('fas fa-file-alt', 'fas fa-file-alt'),
    ('fas fa-file-contract', 'fas fa-file-contract'),
    ('fas fa-file-invoice', 'fas fa-file-invoice'),
    ('fas fa-file-pdf', 'fas fa-file-pdf'),
    ('fas fa-file-signature', 'fas fa-file-signature'),
    ('fas fa-fingerprint', 'fas fa-fingerprint'),
    ('fas fa-fire', 'fas fa-fire'),
    ('fas fa-flag', 'fas fa-flag'),
    ('fas fa-flag-checkered', 'fas fa-flag-checkered'),
    ('fas fa-futbol', 'fas fa-futbol'),
    ('fas fa-gavel', 'fas fa-gavel'),
    ('fas fa-gem', 'fas fa-gem'),
    ('fas fa-globe', 'fas fa-globe'),
    ('fas fa-globe-americas', 'fas fa-globe-americas'),
    ('fas fa-globe-asia', 'fas fa-globe-asia'),
    ('fas fa-graduation-cap', 'fas fa-graduation-cap'),
    ('fas fa-hand-fist', 'fas fa-hand-fist'),
    ('fas fa-hand-holding-dollar', 'fas fa-hand-holding-dollar'),
    ('fas fa-hand-holding-usd', 'fas fa-hand-holding-usd'),
    ('fas fa-hands-helping', 'fas fa-hands-helping'),
    ('fas fa-handshake', 'fas fa-handshake'),
    ('fas fa-headset', 'fas fa-headset'),
    ('fas fa-heartbeat', 'fas fa-heartbeat'),
    ('fas fa-history', 'fas fa-history'),
    ('fas fa-hourglass-half', 'fas fa-hourglass-half'),
    ('fas fa-id-badge', 'fas fa-id-badge'),
    ('fas fa-id-card', 'fas fa-id-card'),
    ('fas fa-info-circle', 'fas fa-info-circle'),
    ('fas fa-landmark', 'fas fa-landmark'),
    ('fas fa-language', 'fas fa-language'),
    ('fas fa-laptop', 'fas fa-laptop'),
    ('fas fa-laptop-code', 'fas fa-laptop-code'),
    ('fas fa-laptop-house', 'fas fa-laptop-house'),
    ('fas fa-layer-group', 'fas fa-layer-group'),
    ('fas fa-leaf', 'fas fa-leaf'),
    ('fas fa-lightbulb', 'fas fa-lightbulb'),
    ('fas fa-link', 'fas fa-link'),
    ('fas fa-list-check', 'fas fa-list-check'),
    ('fas fa-lock', 'fas fa-lock'),
    ('fas fa-magic', 'fas fa-magic'),
    ('fas fa-map-marker-alt', 'fas fa-map-marker-alt'),
    ('fas fa-medal', 'fas fa-medal'),
    ('fas fa-microchip', 'fas fa-microchip'),
    ('fas fa-microphone', 'fas fa-microphone'),
    ('fas fa-microphone-alt', 'fas fa-microphone-alt'),
    ('fas fa-microscope', 'fas fa-microscope'),
    ('fas fa-mobile-alt', 'fas fa-mobile-alt'),
    ('fas fa-money-bill-wave', 'fas fa-money-bill-wave'),
    ('fas fa-mug-hot', 'fas fa-mug-hot'),
    ('fas fa-network-wired', 'fas fa-network-wired'),
    ('fas fa-newspaper', 'fas fa-newspaper'),
    ('fas fa-paper-plane', 'fas fa-paper-plane'),
    ('fas fa-percent', 'fas fa-percent'),
    ('fas fa-phone-alt', 'fas fa-phone-alt'),
    ('fas fa-piggy-bank', 'fas fa-piggy-bank'),
    ('fas fa-pills', 'fas fa-pills'),
    ('fas fa-plane', 'fas fa-plane'),
    ('fas fa-play', 'fas fa-play'),
    ('fas fa-podcast', 'fas fa-podcast'),
    ('fas fa-portrait', 'fas fa-portrait'),
    ('fas fa-project-diagram', 'fas fa-project-diagram'),
    ('fas fa-random', 'fas fa-random'),
    ('fas fa-redo', 'fas fa-redo'),
    ('fas fa-robot', 'fas fa-robot'),
    ('fas fa-rocket', 'fas fa-rocket'),
    ('fas fa-satellite', 'fas fa-satellite'),
    ('fas fa-search', 'fas fa-search'),
    ('fas fa-search-minus', 'fas fa-search-minus'),
    ('fas fa-seedling', 'fas fa-seedling'),
    ('fas fa-server', 'fas fa-server'),
    ('fas fa-shield-alt', 'fas fa-shield-alt'),
    ('fas fa-sitemap', 'fas fa-sitemap'),
    ('fas fa-star', 'fas fa-star'),
    ('fas fa-stethoscope', 'fas fa-stethoscope'),
    ('fas fa-sync-alt', 'fas fa-sync-alt'),
    ('fas fa-table-tennis-paddle-ball', 'fas fa-table-tennis-paddle-ball'),
    ('fas fa-tasks', 'fas fa-tasks'),
    ('fas fa-th', 'fas fa-th'),
    ('fas fa-times', 'fas fa-times'),
    ('fas fa-tools', 'fas fa-tools'),
    ('fas fa-trophy', 'fas fa-trophy'),
    ('fas fa-university', 'fas fa-university'),
    ('fas fa-user', 'fas fa-user'),
    ('fas fa-user-circle', 'fas fa-user-circle'),
    ('fas fa-user-friends', 'fas fa-user-friends'),
    ('fas fa-user-graduate', 'fas fa-user-graduate'),
    ('fas fa-user-shield', 'fas fa-user-shield'),
    ('fas fa-user-tie', 'fas fa-user-tie'),
    ('fas fa-users', 'fas fa-users'),
    ('fas fa-users-cog', 'fas fa-users-cog'),
    ('fas fa-utensils', 'fas fa-utensils'),
    ('fas fa-video', 'fas fa-video'),
    ('fas fa-vr-cardboard', 'fas fa-vr-cardboard'),
    ('fas fa-wallet', 'fas fa-wallet'),
    ('fas fa-wifi', 'fas fa-wifi'),
    ('fas fa-wrench', 'fas fa-wrench')
]

class Program(models.Model):
    title = models.CharField(max_length=255, verbose_name="Yo'nalish nomi")
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name="Slug (URL uchun)")
    icon = models.CharField(max_length=100, verbose_name="Iconka (FontAwesome)", blank=True, null=True,
                            help_text="Masalan: fas fa-briefcase")
    image = models.ImageField(upload_to="programs/", verbose_name="Yo'nalish rasmi", blank=True, null=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, verbose_name="Ta'lim darajasi")
    education_form = models.ForeignKey(EducationForm, on_delete=models.CASCADE, verbose_name="Ta'lim shakli")
    duration = models.CharField(max_length=255, verbose_name="Davomiyligi")
    contract_amount = models.CharField(max_length=255, verbose_name="Kontrakt summasi (qisqa)",
                                       help_text="Masalan: 24 MLN")
    contract_price = models.PositiveIntegerField(default=0, verbose_name="Kontrakt narxi (so'm)",
                                                  help_text="To'liq raqam, masalan: 24000000")
    what_it_gives_text = models.TextField(verbose_name="Dastur sizga nima beradi - matn", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    @property
    def formatted_contract_price(self):
        try:
            return '{:,}'.format(int(self.contract_price)).replace(',', ' ')
        except (ValueError, TypeError):
            return self.contract_price

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"
        ordering = ['order']

class WhatItGivesItem(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="what_it_gives_items")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    icon = models.CharField(max_length=100, verbose_name="Iconka", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Dastur nima beradi (punkt)"
        verbose_name_plural = "Dastur nima beradi (punktlar)"
        ordering = ['order']

class ProgramAdvantage(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="advantages")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    icon = models.CharField(max_length=100, verbose_name="Iconka", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yo'nalish afzalligi"
        verbose_name_plural = "Yo'nalish afzalliklari"
        ordering = ['order']

class ProgramApproach(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    icon = models.CharField(max_length=100, verbose_name="Iconka", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bizning yondashuv"
        verbose_name_plural = "Bizning yondashuv"
        ordering = ['order']

class CampusGallery(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    icon = models.CharField(max_length=100, verbose_name="Iconka", blank=True, null=True,
                            help_text="Masalan: fas fa-handshake")
    image = models.ImageField(upload_to="campus_gallery/", verbose_name="Rasm")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kampus Galereyasi"
        verbose_name_plural = "Kampus Galereyasi"
        ordering = ['order']


class Researcher(models.Model):
    name = models.CharField(max_length=255, verbose_name="F.I.SH.")
    position = models.CharField(max_length=255, verbose_name="Ilmiy daraja va lavozimi")
    education_history = models.TextField(verbose_name="O'quv faoliyati")
    image = models.ImageField(upload_to="researchers/", verbose_name="Rasm")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tadqiqotchi (Olim)"
        verbose_name_plural = "Tadqiqotchilar (Olimlar)"
        ordering = ['order']

class ResearcherAchievement(models.Model):
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE, related_name="achievements")
    title = models.CharField(max_length=500, verbose_name="Yutuq / Ilmiy ish")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ilmiy yutuq"
        verbose_name_plural = "Ilmiy yutuqlar"
        ordering = ['order']


class CouncilMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism")
    surname = models.CharField(max_length=255, verbose_name="Familiya / Otasining ismi")
    position = models.CharField(max_length=255, verbose_name="Lavozimi",
                                help_text="Masalan: Yoshlar yetakchisi")
    motto = models.CharField(max_length=500, verbose_name="Bosh g'oya / Shiori", blank=True, null=True)
    bio = models.TextField(verbose_name="Qisqacha ma'lumot")
    image = models.ImageField(upload_to="council/", verbose_name="Rasm")
    badge_icon = models.CharField(max_length=100, verbose_name="Badge ikonka", blank=True, null=True,
                                  help_text="Masalan: fas fa-crown")
    bg_icon = models.CharField(max_length=100, verbose_name="Fon ikonka (katta)", blank=True, null=True,
                               help_text="Masalan: fas fa-chess-king")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Kengash a'zosi"
        verbose_name_plural = "Kengash a'zolari"
        ordering = ['order']


class Leader(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="F.I.SH.")
    position = models.CharField(max_length=255, verbose_name="Lavozimi",
                                help_text="Masalan: REKTOR, PROREKTOR, BOSH DIREKTOR")
    degree = models.CharField(max_length=255, verbose_name="Ilmiy daraja", blank=True, null=True,
                              help_text="Masalan: Siyosiy fanlar doktori, Professor")
    image = models.ImageField(upload_to="leaders/", verbose_name="Rasm")
    badge_icon = models.CharField(max_length=100, verbose_name="Badge ikonka", blank=True, null=True,
                                  default="fas fa-star", help_text="Masalan: fas fa-star")

    # Aloqa ma'lumotlari
    reception_time = models.CharField(max_length=255, verbose_name="Qabul vaqti", blank=True, null=True,
                                      help_text="Masalan: Seshanba - Payshanba (14:00-16:00)")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    telegram_url = models.URLField(verbose_name="Telegram havola", blank=True, null=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn havola", blank=True, null=True)

    # Biografiya (modal uchun)
    bio_intro = models.TextField(verbose_name="Biografiya kirish matni", blank=True, null=True,
                                 help_text="Umumiy ma'lumot — modal ochilib chiqgandagi bosh matn")
    bio_degree_text = models.TextField(verbose_name="Ilmiy daraja (batafsil)", blank=True, null=True,
                                       help_text="Ilmiy daraja haqida kengaytirilgan ma'lumot")
    bio_research_text = models.TextField(verbose_name="Ilmiy faoliyat (batafsil)", blank=True, null=True,
                                         help_text="Ilmiy ishlari va maqolalari haqida")
    bio_international_text = models.TextField(verbose_name="Xalqaro tajriba (batafsil)", blank=True, null=True,
                                              help_text="Xalqaro konferensiyalar va tajriba haqida")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return f"{self.full_name} — {self.position}"

    class Meta:
        verbose_name = "Rahbar"
        verbose_name_plural = "Rahbariyat"
        ordering = ['order']


class LeaderExperience(models.Model):
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE, related_name="experiences")
    date_range = models.CharField(max_length=100, verbose_name="Sana oralig'i",
                                  help_text="Masalan: 2019-2022 yy.")
    description = models.TextField(verbose_name="Faoliyat tavsifi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return f"{self.date_range} — {self.description[:50]}"

    class Meta:
        verbose_name = "Mehnat faoliyati"
        verbose_name_plural = "Mehnat faoliyati"
        ordering = ['order']


class Department(models.Model):
    TYPE_CHOICES = (
        ('kafedra', 'Kafedra'),
        ('bolim', "Bo'lim"),
    )
    name = models.CharField(max_length=255, verbose_name="Nomi")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Turi")
    
    # Rahbar (Mudir / Boshliq)
    head_name = models.CharField(max_length=255, verbose_name="Boshliq F.I.SH.")
    head_position = models.CharField(max_length=255, verbose_name="Boshliq lavozimi", help_text="M-n: Kafedra mudiri")
    head_image = models.ImageField(upload_to="departments/", verbose_name="Boshliq rasmi")
    description = models.TextField(verbose_name="Tavsif (Biografiya / Malumot)", help_text="Boshliq yoki kafedra haqida batafsil matn")
    
    # Aloqa
    phone = models.CharField(max_length=50, verbose_name="Telefon", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    class Meta:
        verbose_name = "Kafedra / Bo'lim"
        verbose_name_plural = "Kafedralar va Bo'limlar"
        ordering = ['order']


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees", verbose_name="Kafedra/Bo'lim")
    full_name = models.CharField(max_length=255, verbose_name="F.I.SH.")
    position = models.CharField(max_length=255, verbose_name="Lavozimi", help_text="M-n: Kafedra o'qituvchisi")
    image = models.ImageField(upload_to="employees/", verbose_name="Rasm")
    bio = models.TextField(verbose_name="Biografiya")
    
    phone = models.CharField(max_length=50, verbose_name="Telefon", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        ordering = ['order']

class NewsCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Turkum nomi", help_text="M-n: Yangiliklar, Tahliliy materiallar")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL Slug")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik turkumi"
        verbose_name_plural = "Yangilik turkumlari"
        ordering = ['order']

class News(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news_set', verbose_name="Turkum")
    title = models.CharField(max_length=500, verbose_name="Sarlavha")
    slug = models.SlugField(max_length=500, unique=True, verbose_name="URL Slug")
    image = models.ImageField(upload_to="news/", verbose_name="Ro'yxat sahifasi rasmi (Asosiy)")
    detail_image = models.ImageField(upload_to="news/details/", null=True, blank=True, verbose_name="Batafsil sahifa rasmi (Ichkari)")
    
    badge = models.CharField(max_length=100, blank=True, null=True, verbose_name="Yorliq (Badge)", help_text="M-n: Dolzarb, Xalqaro")
    
    excerpt = models.TextField(verbose_name="Qisqacha matn", help_text="Sahifada ro'yxatda ko'rinadigan qisqacha mazmun")
    content = models.TextField(verbose_name="To'liq matn")
    
    author = models.CharField(max_length=255, default="Matbuot Xizmati", verbose_name="Muallif yoki bo'lim")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    
    published_date = models.DateField(verbose_name="Chop etilgan sana")
    is_published = models.BooleanField(default=True, verbose_name="Saytda ko'rinishi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-published_date', '-id']

class Slider(models.Model):
    STYLE_CHOICES = (
        ('style_1', 'Video fon (1-slayd uslubi)'),
        ('style_2', 'Cyber va Rasm (2-slayd uslubi)'),
        ('style_3', 'Prestige va Qo\'shimcha karta (3-slayd uslubi)'),
        ('style_4', 'Gradient va Uchta blok (4-slayd uslubi)'),
    )
    style = models.CharField("Slayd uslubi", max_length=20, choices=STYLE_CHOICES, default='style_1')
    order = models.PositiveIntegerField("Tartib raqami", default=0)
    is_active = models.BooleanField("Faol", default=True)

    # Umumiy matnlar
    badge_text = models.CharField("Nishon matni (Badge)", max_length=150, blank=True)
    title_part_1 = models.CharField("Sarlavha 1-qismi", max_length=150)
    title_part_2 = models.CharField("Sarlavha ajratilgan qismi (Highlight/Glitch)", max_length=150, blank=True)
    title_part_3 = models.CharField("Sarlavha 3-qismi", max_length=150, blank=True)
    description = models.TextField("Tavsif", blank=True, null=True)
    button_text = models.CharField("Tugma matni", max_length=100, default="BATAFSIL", blank=True)
    modal_target = models.CharField("Modal Oyna ID", max_length=50, blank=True)
    
    # Media fayllar
    background_image = models.ImageField("Orqa fon rasmi", upload_to="sliders/", blank=True, null=True)
    background_video = models.FileField("Orqa fon videoga (Faqat 1-uslub)", upload_to="sliders/", blank=True, null=True)
    video_poster = models.ImageField("Video poster (Cover)", upload_to="sliders/", blank=True, null=True)

    def __str__(self):
        return f"{self.title_part_1} ({self.get_style_display()})"

    class Meta:
        verbose_name = "Slayder"
        verbose_name_plural = "Slayderlar"
        ordering = ['order']

class SliderFeature(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='features')
    icon = models.CharField("Ikonka klassi (Masalan: fas fa-rocket)", max_length=100, blank=True)
    title = models.CharField("Sarlavha", max_length=150)
    description = models.CharField("Qisqacha matni", max_length=255, blank=True)
    order = models.PositiveIntegerField("Tartib raqami", default=0)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Qo'shimcha kartochka (3 va 4 uslub uchun)"
        verbose_name_plural = "Qo'shimcha kartochkalar (Faqat 3 va 4 uslublarda ishlaydi)"
        ordering = ['order']

class SliderModalItem(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='modal_items')
    icon = models.CharField("Ikonka (Masalan: fas fa-rocket)", max_length=100, blank=True)
    title = models.CharField("Sarlavha", max_length=150)
    description = models.TextField("Matni", blank=True)
    order = models.PositiveIntegerField("Tartib raqami", default=0)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Modal ichki kartochkasi"
        verbose_name_plural = "Modal ichki kartochkalari"
        ordering = ['order']


class FAQCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Turkum nomi", help_text="Masalan: Qabul, Moliya")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Tab Slug (Inglizcha, kichik harfda)")
    icon = models.CharField(max_length=100, verbose_name="Turkum Ikonkasi", help_text="Masalan: fas fa-file-alt")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "FAQ Turkumi"
        verbose_name_plural = "FAQ Turkumlari"
        ordering = ['order']

class FAQItem(models.Model):
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, related_name="faqs", verbose_name="Turkum")
    question = models.CharField(max_length=500, verbose_name="Savol")
    answer = models.TextField(verbose_name="Javob", help_text="HTML teglar (masalan: <strong>, <a>) ishlatish mumkin")
    icon = models.CharField(max_length=100, verbose_name="Savol Ikonkasi", help_text="Masalan: fas fa-calendar-check", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi (Saytda ko'rinadimi)?")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ Savol"
        verbose_name_plural = "FAQ Savollar"
        ordering = ['order', 'id']

import uuid

class ChatConversation(models.Model):
    session_key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, verbose_name="Sessiya kaliti")
    fullname = models.CharField(max_length=255, verbose_name="Ism va Familiya")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    def __str__(self):
        return f"{self.fullname} ({self.phone})"

    @property
    def unread_count(self):
        return self.messages.filter(is_from_admin=False, is_read=False).count()

    class Meta:
        verbose_name = "Chat suhbat"
        verbose_name_plural = "Chat suhbatlar"
        ordering = ['-updated_at']


class ChatMessage(models.Model):
    conversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE, related_name='messages', verbose_name="Suhbat")
    text = models.TextField(verbose_name="Xabar matni")
    is_from_admin = models.BooleanField(default=False, verbose_name="Admin tomonidan")
    is_read = models.BooleanField(default=False, verbose_name="O'qilganmi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")

    def __str__(self):
        sender = "Admin" if self.is_from_admin else self.conversation.fullname
        return f"{sender}: {self.text[:50]}"

    class Meta:
        verbose_name = "Chat xabar"
        verbose_name_plural = "Chat xabarlar"
        ordering = ['created_at']

class Partner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Hamkor nomi", blank=True, null=True)
    image = models.ImageField(upload_to="partners/", verbose_name="Hamkor raqsi (Logosi)")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title or f"Hamkor #{self.id}"

    class Meta:
        verbose_name = "Hamkor"
        verbose_name_plural = "Hamkorlar"
        ordering = ['order', '-id']


class ShopCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug (URL uchun)")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Do'kon kategoriyasi"
        verbose_name_plural = "Do'kon kategoriyalari"
        ordering = ['order']


class ShopProduct(models.Model):
    BADGE_CHOICES = (
        ('', 'Yo\'q'),
        ('YANGI', 'YANGI'),
        ('HOT', 'HOT'),
        ('-10%', '-10%'),
        ('-15%', '-15%'),
        ('-20%', '-20%'),
        ('-25%', '-25%'),
        ('-30%', '-30%'),
        ('-50%', '-50%'),
    )
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, related_name='products', verbose_name="Kategoriya")
    title = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    image = models.ImageField(upload_to="shop/", verbose_name="Rasm")
    price = models.PositiveIntegerField(verbose_name="Narxi (so'm)")
    old_price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Eski narxi (so'm)",
                                             help_text="Chegirma bo'lsa eski narxni kiriting")
    badge = models.CharField(max_length=50, blank=True, default='', verbose_name="Yorliq (Badge)",
                              choices=BADGE_CHOICES, help_text="Masalan: YANGI, -15%")
    rating = models.PositiveIntegerField(default=5, verbose_name="Reyting (1-5)",
                                          help_text="1 dan 5 gacha yulduz")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi (saytda ko'rinadimi)?")
    created_at = models.DateField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqam")

    @property
    def formatted_price(self):
        return '{:,}'.format(self.price).replace(',', ',')

    @property
    def formatted_old_price(self):
        if self.old_price:
            return '{:,}'.format(self.old_price).replace(',', ',')
        return ''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Do'kon mahsuloti"
        verbose_name_plural = "Do'kon mahsulotlari"
        ordering = ['order', '-created_at']


class ShopProductColor(models.Model):
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, related_name='colors', verbose_name="Mahsulot")
    name = models.CharField(max_length=100, verbose_name="Rang nomi", help_text="Masalan: Oq, Qora, Qizil")
    image = models.ImageField(upload_to="shop/colors/", verbose_name="Rang rasmi", help_text="Ushbu rang uchun mahsulot rasmi")

    def __str__(self):
        return f"{self.product.title} - {self.name}"

    class Meta:
        verbose_name = "Mahsulot rangi"
        verbose_name_plural = "Mahsulot ranglari"


class ShopProductSize(models.Model):
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, related_name='sizes', verbose_name="Mahsulot")
    name = models.CharField(max_length=50, verbose_name="O'lcham", help_text="Masalan: S, M, L, XL, XXL, 42, 44")

    def __str__(self):
        return f"{self.product.title} - {self.name}"

    class Meta:
        verbose_name = "Mahsulot o'lchami"
        verbose_name_plural = "Mahsulot o'lchamlari"


class ShopOrder(models.Model):
    STATUS_CHOICES = (
        ('new', 'Yangi (Kutilmoqda)'),
        ('processing', 'Jarayonda'),
        ('shipped', 'Yetkazilmoqda'),
        ('completed', 'Tugallangan/Yetkazib berilgan'),
        ('cancelled', 'Bekor qilingan'),
    )
    full_name = models.CharField(max_length=255, verbose_name="F.I.SH")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
    address = models.TextField(blank=True, verbose_name="Manzili (Yetkazib berish uchun)")
    total_price = models.PositiveIntegerField(default=0, verbose_name="Jami summa (so'm)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Holati")
    note = models.TextField(blank=True, null=True, verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Buyurtma vaqti")

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.full_name} ({self.status})"

    class Meta:
        verbose_name = "Do'kon buyurtmasi"
        verbose_name_plural = "Do'kon buyurtmalari"
        ordering = ['-created_at']


class ShopOrderItem(models.Model):
    order = models.ForeignKey(ShopOrder, on_delete=models.CASCADE, related_name='items', verbose_name="Buyurtma")
    product = models.ForeignKey(ShopProduct, on_delete=models.SET_NULL, null=True, verbose_name="Mahsulot")
    product_name = models.CharField(max_length=255, verbose_name="Mahsulot nomi (Saqlangan)")
    color = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tanlangan rang")
    size = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tanlangan o'lcham")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Soni")
    price = models.PositiveIntegerField(verbose_name="Donasining narxi (so'm)")
    
    @property
    def total_price(self):
        qty = self.quantity or 0
        prc = self.price or 0
        return qty * prc

    def __str__(self):
        return f"{self.product_name} x{self.quantity}"

    class Meta:
        verbose_name = "Buyurtma qilingan mahsulot"
        verbose_name_plural = "Buyurtma qilingan mahsulotlar"


class ProgramApplication(models.Model):
    STATUS_CHOICES = (
        ('new', 'Yangi'),
        ('contacted', "Bog'lanildi"),
        ('completed', 'Yakunlandi'),
    )
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="applications", verbose_name="Yo'nalish")
    first_name = models.CharField(max_length=255, verbose_name="Ism")
    last_name = models.CharField(max_length=255, verbose_name="Familiya")
    middle_name = models.CharField(max_length=255, verbose_name="Sharif", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Holat")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ariza vaqti")

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.program.title if self.program else 'Nomalum'}"

    class Meta:
        verbose_name = "Yo'nalish arizasi"
        verbose_name_plural = "Yo'nalish arizalari"
        ordering = ['-created_at']
