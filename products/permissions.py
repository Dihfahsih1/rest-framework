from rest_framework import permissions

class IsStaffEditorPemission(permissions.DjangoModelPermissions):
  def has_permission(self, request, view):
    user = request
    print(user.get_all_permissions())
    if user.is_staff:
      if user.has_perm("products.add_product()"):
        return True
      
      if user.has_perm("products.view_product()"):
        return True
      
      if user.has_perm("products.change_product()"):
        return True
      
      if user.has_perm("products.delete_product()"):
        return True
      return False
    return False