from modeltranslation.translator import register,TranslationOptions,translator
from .models import *

@register(Mahsulotlar)
class MahsulotlarTranslationOptions(TranslationOptions):
    fields=('sarlavha','text')


@register(Xodimlar)
class XodimlarTranslationOptions(TranslationOptions):
    fields=('ismfamilya','kasbi')

@register(AboutAwards)
class AboutAwardsTranslationOptions(TranslationOptions):
    fields=('sarlavha','sarlavha1','text')


@register(AboutName)
class AboutNameTranslationOptions(TranslationOptions):
    fields=('title','li1','li2','li3')

@register(BizningMahsulot)
class BizningMahsulotTranslationOptions(TranslationOptions):
    fields = ('nomi','date')

@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ('addres','pochta')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields=('title','text')