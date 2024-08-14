from typing import Any

import pytest

from model_bakery import baker
from django.db import models

DATETIME_FIELDS = (models.DateTimeField, models.DateField, models.TimeField)


class ModelTest:
    model: models.Model = None

    instance_kwargs: dict[str, Any] = {}

    @pytest.fixture
    def instance(self) -> models.Model:
        return baker.make(self.model, **self.instance_kwargs)

    def test_issubclass_model(self) -> None:
        assert issubclass(self.model, models.Model)


class FieldBoolModelTest:
    model: models.Model = None
    field_name: str = None
    field_type: models.Field = None

    null: bool = False
    blank: bool = False
    unique: bool = False
    db_index: bool = False
    auto_now: bool = False
    auto_now_add: bool = False

    @property
    def field(self):
        return self.model._meta.get_field(self.field_name)

    def test_field_type(self):
        assert isinstance(self.field, self.field_type)

    def test_is_null(self):
        assert self.field.null == self.null

    def test_is_blank(self):
        assert self.field.blank == self.blank

    def test_is_unique(self):
        assert self.field.unique == self.unique

    def test_is_db_index(self):
        assert self.field.db_index == self.db_index

    def test_is_auto_now(self):
        if self.field.__class__ not in DATETIME_FIELDS:
            pytest.skip(f"{self.model.__name__}->{self.field_name} is not a date/time model type.")

        assert self.field.auto_now == self.auto_now

    def test_is_auto_now_add(self):
        if self.field.__class__ not in DATETIME_FIELDS:
            pytest.skip(f"{self.model.__name__}->{self.field_name} is not a date/time model type.")

        assert self.field.auto_now_add == self.auto_now_add


class FieldVerboseNameModelTest:
    model: models.Model = None
    field_name: str = None
    verbose_name: str = None

    @property
    def field(self):
        return self.model._meta.get_field(self.field_name)

    def test_verbose_name(self):
        assert self.field.verbose_name == self.verbose_name


class FieldDigitsModelTest:
    model: models.Model = None
    field_name: str = None

    max_length: int = None
    decimal_places: int = None
    max_digits: int = None

    @property
    def field(self):
        return self.model._meta.get_field(self.field_name)

    def test_max_length(self):
        if not self.max_length:
            pytest.skip(f'Field {self.field_name} is not apply')

        assert self.field.max_length == self.max_length

    def test_decimal_places(self):
        if not self.decimal_places:
            pytest.skip(f'Field {self.field_name} is not apply')

        assert self.field.decimal_places == self.decimal_places

    def test_max_digits(self):
        if not self.max_digits:
            pytest.skip(f'Field {self.field_name} is not apply')

        assert self.field.max_digits == self.max_digits
