"""
© Ocado Group
Created on 03/04/2024 at 16:37:44(+01:00).
"""

from django_filters import (  # type: ignore[import-untyped] # isort: skip
    rest_framework as filters,
)

from ..models import User


# pylint: disable-next=missing-class-docstring
class UserFilterSet(filters.FilterSet):
    students_in_class = filters.CharFilter(
        "new_student__class_field__access_code",
        "exact",
    )

    class Meta:
        model = User
        fields = ["students_in_class"]
