from django.contrib import admin
from posts.models import Post

# Register your models here.


# class CommentsInline(admin.StackedInline):
# 	model = Comments
# 	extra = 1


class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		('Create Post', {'fields': ['title', 'author', 'matric_no', 'body']}),
		('Date information', {'fields': ['pub_date']}),
	]


	list_display = ('__str__', 'author', 'matric_no', 'pub_date')
	search_fields = ['author', 'title']


	# inlines = [CommentsInline]


admin.site.register(Post, PostAdmin)


