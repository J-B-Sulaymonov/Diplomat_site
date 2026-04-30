from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline, TranslationTabularInline
from .models import Program, WhatItGivesItem, ProgramAdvantage, ProgramApproach, Degree, EducationForm, CampusGallery, Researcher, ResearcherAchievement, CouncilMember, Leader, LeaderExperience, Department, Employee, NewsCategory, News, Slider, SliderFeature, SliderModalItem, FAQCategory, FAQItem, ChatConversation, ChatMessage, Partner, ProgramApplication, ShopCategory, ShopProduct, ShopProductColor, ShopProductSize, ShopOrder, ShopOrderItem

@admin.register(Degree)
class DegreeAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(EducationForm)
class EducationFormAdmin(TranslationAdmin):
    list_display = ('title',)

class WhatItGivesItemInline(TranslationStackedInline):
    model = WhatItGivesItem
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
    }

class ProgramAdvantageInline(TranslationStackedInline):
    model = ProgramAdvantage
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
    }



@admin.register(Program)
class ProgramAdmin(TranslationAdmin):
    list_display = ('order', 'title', 'icon', 'degree', 'education_form', 'duration', 'contract_amount', 'contract_price')
    list_editable = ('order',)
    list_display_links = ('title',)
    search_fields = ('title', 'degree__title', 'education_form__title')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [WhatItGivesItemInline, ProgramAdvantageInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 5})},
    }

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
                'admin/css/iconpicker_custom.css',
            )
        }
        js = (
            'admin/js/iconpicker_init.js',
        )

@admin.register(CampusGallery)
class CampusGalleryAdmin(TranslationAdmin):
    list_display = ('order', 'title', 'icon', 'image')
    list_editable = ('order',)
    list_display_links = ('title',)
    search_fields = ('title',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
    }

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
                'admin/css/iconpicker_custom.css',
            )
        }
        js = (
            'admin/js/iconpicker_init.js',
        )

class ResearcherAchievementInline(TranslationStackedInline):
    model = ResearcherAchievement
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
    }

@admin.register(Researcher)
class ResearcherAdmin(TranslationAdmin):
    list_display = ('order', 'name', 'position')
    list_editable = ('order',)
    list_display_links = ('name',)
    search_fields = ('name', 'position')
    inlines = [ResearcherAchievementInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 3})},
    }

@admin.register(CouncilMember)
class CouncilMemberAdmin(TranslationAdmin):
    list_display = ('order', 'name', 'surname', 'position', 'badge_icon')
    list_editable = ('order',)
    list_display_links = ('name',)
    search_fields = ('name', 'surname', 'position')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 3})},
    }

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
                'admin/css/iconpicker_custom.css',
            )
        }
        js = (
            'admin/js/iconpicker_init.js',
        )

class LeaderExperienceInline(TranslationStackedInline):
    model = LeaderExperience
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 2})},
    }

@admin.register(Leader)
class LeaderAdmin(TranslationAdmin):
    list_display = ('order', 'full_name', 'position', 'degree', 'phone')
    list_editable = ('order',)
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'position')
    inlines = [LeaderExperienceInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 4})},
    }

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
                'admin/css/iconpicker_custom.css',
            )
        }
        js = (
            'admin/js/iconpicker_init.js',
        )

class EmployeeInline(TranslationStackedInline):
    model = Employee
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }

@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ('order', 'name', 'type', 'head_name')
    list_editable = ('order',)
    list_display_links = ('name',)
    list_filter = ('type',)
    search_fields = ('name', 'head_name')
    inlines = [EmployeeInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }

@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('order', 'title', 'slug')
    list_editable = ('order',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

from django import forms

class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'image_position_y': forms.NumberInput(attrs={
                'type': 'range', 
                'min': '0', 
                'max': '100', 
                'step': '1', 
                'style': 'width: 100%; max-width: 400px; margin-top: 5px;',
                'oninput': 'document.getElementById("main_pos_val").innerText = this.value + "%"'
            }),
            'detail_image_position_y': forms.NumberInput(attrs={
                'type': 'range', 
                'min': '0', 
                'max': '100', 
                'step': '1', 
                'style': 'width: 100%; max-width: 400px; margin-top: 5px;',
                'oninput': 'document.getElementById("pos_val").innerText = this.value + "%"'
            }),
        }

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    form = NewsAdminForm
    list_display = ('title', 'category', 'published_date', 'views_count', 'is_published')
    list_display_links = ('title',)
    list_filter = ('category', 'is_published', 'published_date')
    search_fields = ('title', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }

class SliderFeatureInline(TranslationStackedInline):
    model = SliderFeature
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
    }

class SliderModalItemInline(TranslationStackedInline):
    model = SliderModalItem
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 3})},
    }

@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    list_display = ('order', 'title_part_1', 'style', 'is_active')
    list_display_links = ('title_part_1',)
    list_editable = ('order', 'is_active')
    list_filter = ('style', 'is_active')
    search_fields = ('title_part_1', 'badge_text')
    inlines = [SliderFeatureInline, SliderModalItemInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 3})},
    }
    
    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
                'admin/css/iconpicker_custom.css',
            )
        }
        js = (
            'admin/js/iconpicker_init.js',
        )

class FAQItemInline(TranslationStackedInline):
    model = FAQItem
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 4})},
    }

@admin.register(FAQCategory)
class FAQCategoryAdmin(TranslationAdmin):
    list_display = ('order', 'title', 'slug', 'icon')
    list_editable = ('order', 'icon')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    inlines = [FAQItemInline]


class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 1
    fields = ('text', 'is_from_admin', 'is_read', 'created_at')
    readonly_fields = ('created_at',)

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('created_at')


@admin.register(ChatConversation)
class ChatConversationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'email', 'unread_count_display', 'message_count', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('fullname', 'phone', 'email')
    readonly_fields = ('session_key', 'fullname', 'phone', 'email', 'created_at', 'updated_at')

    def unread_count_display(self, obj):
        count = obj.unread_count
        if count > 0:
            return f"🔴 {count} ta yangi"
        return "✅ O'qilgan"
    unread_count_display.short_description = "Holat"

    def message_count(self, obj):
        return obj.messages.count()
    message_count.short_description = "Xabarlar"

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        conversation = ChatConversation.objects.get(pk=object_id)
        messages = conversation.messages.all().order_by('created_at')

        # Foydalanuvchi xabarlarini o'qilgan deb belgilash
        conversation.messages.filter(is_from_admin=False, is_read=False).update(is_read=True)

        extra_context['conversation'] = conversation
        extra_context['messages'] = messages
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'image')
    list_editable = ('order',)
    list_display_links = ('title',)
    search_fields = ('title',)

@admin.register(ProgramApproach)
class ProgramApproachAdmin(TranslationAdmin):
    list_display = ('order', 'title', 'icon')
    list_editable = ('order',)
    list_display_links = ('title',)
    search_fields = ('title',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
        models.TextField: {'widget': Textarea(attrs={'class': 'form-control', 'rows': 4})},
    }

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
                'admin/css/iconpicker_custom.css',
            )
        }
        js = (
            'admin/js/iconpicker_init.js',
        )

@admin.register(ProgramApplication)
class ProgramApplicationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'first_name', 'last_name', 'phone', 'program', 'status')
    list_display_links = ('first_name', 'last_name')
    list_filter = ('status', 'program', 'created_at')
    list_editable = ('status',)
    search_fields = ('first_name', 'last_name', 'phone')
    readonly_fields = ('first_name', 'last_name', 'middle_name', 'phone', 'program', 'created_at')
    date_hierarchy = 'created_at'


class ShopProductInline(TranslationStackedInline):
    model = ShopProduct
    extra = 1
    fields = ('title', 'image', 'price', 'old_price', 'badge', 'rating', 'is_active', 'order')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
    }

@admin.register(ShopCategory)
class ShopCategoryAdmin(TranslationAdmin):
    list_display = ('order', 'title', 'slug', 'product_count')
    list_editable = ('order',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    inlines = [ShopProductInline]

    def product_count(self, obj):
        return obj.products.filter(is_active=True).count()
    product_count.short_description = "Mahsulotlar soni"

@admin.register(ShopProduct)
class ShopProductAdmin(TranslationAdmin):
    list_display = ('order', 'title', 'category', 'price', 'old_price', 'badge', 'rating', 'is_active')
    list_editable = ('order', 'price', 'old_price', 'badge', 'is_active')
    list_display_links = ('title',)
    list_filter = ('category', 'is_active', 'badge')
    search_fields = ('title',)
    inlines = []
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'form-control'})},
    }

class ShopProductColorInline(TranslationTabularInline):
    model = ShopProductColor
    extra = 1

class ShopProductSizeInline(TranslationTabularInline):
    model = ShopProductSize
    extra = 1

# Add the new inlines to the existing ShopProductAdmin registered above
ShopProductAdmin.inlines = [ShopProductColorInline, ShopProductSizeInline]


class ShopOrderItemInline(admin.TabularInline):
    model = ShopOrderItem
    extra = 0
    readonly_fields = ('product_name', 'color', 'size', 'quantity', 'price', 'total_price')
    can_delete = False

@admin.register(ShopOrder)
class ShopOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'phone', 'id')
    readonly_fields = ('created_at',)
    list_editable = ('status',)
    inlines = [ShopOrderItemInline]
