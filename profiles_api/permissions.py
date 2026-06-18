from rest_framework import permissions

# UpdateOwnProfile is a custom permission class that enforces ownership rules — users can only modify their own profile, but everyone can read profiles.
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id