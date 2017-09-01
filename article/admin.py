from django.contrib import admin

from article.models import Author, Tag, Classification, Article, Customer
# Register your models here.
# from django_summernote.admin import SummernoteModelAdmin
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Classification)
admin.site.register(Customer)

# class ArticleAdmin(SummernoteModelAdmin):
# pass
# admin.site.register(Article,ArticleAdmin)

class ArticleAdmin(admin.ModelAdmin):
	class Media:
		js = (

			'/static/tinymce/tinymce.min.js',
			'/static/tinymce/config.js',

		)


admin.site.register(Article, ArticleAdmin)
