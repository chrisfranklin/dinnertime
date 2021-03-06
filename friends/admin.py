from django.contrib import admin

from friends.models import Friendship, FriendshipInvitation, Blocking, FriendList


class FriendshipAdmin(admin.ModelAdmin):
    """
    Lists all friendships
    """
    list_display = ["id", "from_user", "to_user", "added"]

class FriendshipInvitationAdmin(admin.ModelAdmin):
    """
    Lists all friendship invitations
    """
    list_display = ["id", "from_user", "to_user", "sent"]


class BlockingAdmin(admin.ModelAdmin):
    """
    Lists blocked users for all users
    """
    list_display = ["id", "from_user", "to_user", "added"]

class FriendListAdmin(admin.ModelAdmin):
    """
    Lists friends for a specific user
    """
    list_display = ["id", "title", "owner"]
    list_display_links = ["id", "title"]
    filter_horizontal = ["friends"]
    search_fields = ["^owner__username", "^title"]
    readonly_fields = ["owner"]


admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(FriendshipInvitation, FriendshipInvitationAdmin)
admin.site.register(Blocking, BlockingAdmin)
admin.site.register(FriendList, FriendListAdmin)
