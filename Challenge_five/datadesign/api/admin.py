from django.contrib import admin
from api.models import User, Agent, Event, Group, GroupUser

# Register your models here.


class UserModeEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_login', 'email', 'password')


class AgentModelEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'env', 'version', 'address')


class EventModeEvent(admin.ModelAdmin):
    list_display = ('id', 'level', 'data', 'arquivado', 'date', 'agent', 'user')


class GroupUserModeEvent(admin.ModelAdmin):
    list_display = ('id', 'group', 'user')


class GroupModeEvent(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(User, UserModeEvent)
admin.site.register(Agent, AgentModelEvent)
admin.site.register(Event, EventModeEvent)
admin.site.register(Group, GroupModeEvent)
admin.site.register(GroupUser, GroupUserModeEvent)