from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from users.models import CustomUser
from users.forms import UserCreationForm, UserChangeForm
from django.contrib import admin, messages

# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    search_fields = ('matric_no',)
    ordering = ('matric_no',)
    filter_horizontal = ('permissions',)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'permissions':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs['queryset'] = qs.select_related('content_type')
        return super(GroupAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


def add_one(modelaadmin, request, queryset):
	for user in queryset:
		if user.part < 6:
			user.part += 1
		else:
			user.part = 6
			user.is_alumni = True
			user.is_active = False
			user.is_exco = False
			user.is_staff = False
			user.is_superuser = False
		user.save()
add_one.short_description = 'Increase level'

class UserAdmin(BaseUserAdmin):
	"""The form to add or change user instances"""
	form = UserChangeForm
	add_form = UserCreationForm
	change_password_form = AdminPasswordChangeForm

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
    
	list_display = ('matric_no', 'surname', 'first_name', 'other_name', 
					'email', 'part', 'phone', 'is_exco',)
	list_filter = ('is_exco', 'is_staff', 'is_superuser', 'part', 'is_alumni', 'groups')
	search_fields = ('first_name', 'surname', 'email', 'matric_no')
	ordering = ('matric_no',)
	actions = [add_one,]
	filter_horizontal = ('groups', 'user_permissions',)

	#add_form_template = 'users/add_form.html'
	change_user_password_template = None
	fieldsets = (
		(None, {'fields': ('matric_no', 'password')}),
		(('Personal info'), {'fields': ('surname','first_name', 'other_name', 'email', 'part',)}),
		(('Permissions'), {'fields': ('is_active', 'is_exco', 'is_staff', 'is_superuser',
										 'groups', 'user_permissions', 'is_alumni',)}),
		(('Extra info'), {'fields': ('gender', 'birth_date', 'image', 'bio')}),
		(('Dates'), {'fields': ('last_login',)}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('surname','first_name', 'other_name', 'email', 'matric_no', 'password',)
		}),
	)

admin.site.register(CustomUser, UserAdmin)