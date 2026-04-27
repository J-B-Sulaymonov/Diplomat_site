from modeltranslation.translator import register, TranslationOptions
from .models import Program, WhatItGivesItem, ProgramAdvantage, ProgramApproach, Degree, EducationForm, CampusGallery, Researcher, ResearcherAchievement, CouncilMember, Leader, LeaderExperience, Department, Employee, NewsCategory, News, Slider, SliderFeature, SliderModalItem, FAQCategory, FAQItem, ShopCategory, ShopProduct, ShopProductColor, ShopProductSize

@register(Degree)
class DegreeTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(EducationForm)
class EducationFormTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'duration', 'contract_amount', 'what_it_gives_text')

@register(WhatItGivesItem)
class WhatItGivesItemTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ProgramAdvantage)
class ProgramAdvantageTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ProgramApproach)
class ProgramApproachTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(CampusGallery)
class CampusGalleryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Researcher)
class ResearcherTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'education_history')

@register(ResearcherAchievement)
class ResearcherAchievementTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(CouncilMember)
class CouncilMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'position', 'motto', 'bio')

@register(Leader)
class LeaderTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'degree', 'reception_time', 'bio_intro', 'bio_degree_text', 'bio_research_text', 'bio_international_text')

@register(LeaderExperience)
class LeaderExperienceTranslationOptions(TranslationOptions):
    fields = ('date_range', 'description')

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'head_name', 'head_position', 'description')

@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'bio')

@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'badge', 'excerpt', 'content', 'author')

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('badge_text', 'title_part_1', 'title_part_2', 'title_part_3', 'description', 'button_text')

@register(SliderFeature)
class SliderFeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(SliderModalItem)
class SliderModalItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(FAQCategory)
class FAQCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(FAQItem)
class FAQItemTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

@register(ShopCategory)
class ShopCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ShopProduct)
class ShopProductTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ShopProductColor)
class ShopProductColorTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ShopProductSize)
class ShopProductSizeTranslationOptions(TranslationOptions):
    fields = ('name',)
