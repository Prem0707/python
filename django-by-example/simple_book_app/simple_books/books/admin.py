from django.contrib import admin

# Register your models here.
from . import models

class Bookadmin(admin.ModelAdmin):
    short_description = '书籍'
    list_display = ('id', 'name', 'publisher', 'publisher_date', 'publisher_state')
    search_fields = ('name',)
    list_filter = ('publisher', 'publisher_date',)
    list_per_page = 5
    list_editable = ('publisher_state',)
    list_select_related = ('publisher',)
    filter_horizontal = ('authors',)
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
    actions = ['set_publisher_checkout', 'set_publisher_dai', 'set_publisher_status', 'set_publisher_del', ]

    def set_publisher_checkout(modeladmin, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)  # 选中传入的表单中,勾选的checkbox对应的id集合
        models.Book.objects.filter(id__in=selected).update(publisher_state='checkout')  # 将所有选中的id对象,修改出版状态为checkout

    def set_publisher_dai(modeladmin, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).update(publisher_state='dai')

    def set_publisher_status(modeladmin, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).update(publisher_state='status')

    def set_publisher_del(modeladmin, request, queryset):  #########扩展部分,增加对选中的记录今夕删除!###########
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).delete()

    set_publisher_checkout.short_description = "设置所有的书籍为--已出版"  # 为了使界面更加友好,添加别名
    set_publisher_status.short_description = "设置所有的书籍为--审核中"
    set_publisher_dai.short_description = "设置所有的书籍为--待出版"
    set_publisher_del.short_description = "设置所有的书籍为--删除"
class Authoradmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')

class Publisheradmin(admin.ModelAdmin):
    list_display = ('name','address','country',)



admin.site.register(models.Author, Authoradmin)
admin.site.register(models.Publisher, Publisheradmin)
admin.site.register(models.Book, Bookadmin)