from django.contrib import admin
from api.models import User, Agent, Event, Group

# Register your models here.


class UserModeEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'last_login')


class AgentModelEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'address', 'status', 'env', 'version')


class EventModeEvent(admin.ModelAdmin):
    list_display = ('id', 'level', 'data', 'agent', 'arquivado', 'date')


class GroupModeEvent(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(User, UserModeEvent)
admin.site.register(Agent, AgentModelEvent)
admin.site.register(Event, EventModeEvent)
admin.site.register(Group, GroupModeEvent)