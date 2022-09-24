from types import prepare_class
from rest_framework import permissions

from .permissions import IsStaffEditorPemission

class StaffEditorPermissions():
  prepare_classes=[permissions.IsAdminUser,
                   IsStaffEditorPemission]