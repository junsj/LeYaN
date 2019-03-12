from django.contrib import admin

from website import models

# Register your models here.


class Category_admin(admin.ModelAdmin):
	list_display = ('id','cid','cname','cgroup')

admin.site.register(models.Category,Category_admin)
admin.site.register(models.Pics)
admin.site.register(models.Albums)
admin.site.register(models.ONE)
admin.site.register(models.Article)
