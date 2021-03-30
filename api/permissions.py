from rest_framework import permissions

# 수정 권한 추가
class IsOwnerOrReadOnly(permissions.BasePermission):
    # 작성자만 접근, 작성자가 아니면 read만 가능
    def has_object_permission(self, request, view, obj):
        # 값을 바꾸지 않는 안전한 method
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user