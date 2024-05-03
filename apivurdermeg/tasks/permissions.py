from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Teachers can view and modify; others can only view.
        return request.method in permissions.SAFE_METHODS or request.user.is_teacher

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only the student who owns the response or the teacher can modify it.
        return (
            request.method in permissions.SAFE_METHODS or
            obj.student == request.user or
            request.user.is_teacher
        )
