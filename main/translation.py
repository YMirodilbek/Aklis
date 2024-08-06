from modeltranslation.translator import register,TranslationOptions,translator
from .models import *

@register(Mahsulotlar)
class MahsulotlarTranslationOptions(TranslationOptions):
    fileds=('sarlavha','text')


@register(Xodimlar)
class XodimlarTranslationOptions(TranslationOptions):
    fileds=('ismfamilya','kasbi')

@register(AboutAwards)
class AboutAwardsTranslationOptions(TranslationOptions):
    fields=('sarlavha','sarlavha1','text')


@register(AboutName)
class AboutNameTranslationOptions(TranslationOptions):
    fields=('title','li1','li2','li3')

@register(BizningMahsulot)
class BizningMahsulotTranslationOptions(TranslationOptions):
    fields = ('nomi','date')