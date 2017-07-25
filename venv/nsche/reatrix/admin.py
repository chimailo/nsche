from django.contrib import admin
from reatrix.models import Article

# Register your models here.


# class CommentsInline(admin.StackedInline):
# 	model = Comments
# 	extra = 1


class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Create Article', {'fields': ['title', 'author', 'body']}),
		#('Date information', {'fields': ['pub_date']}),
	]


	list_display = ('__str__', 'author', 'matric_no', 'pub_date')
	list_filter = ['title', 'author']
	search_fields = ['author', 'title']


	# inlines = [CommentsInline]


admin.site.register(Article, ArticleAdmin)


