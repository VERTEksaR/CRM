import pytest
from django.test import TestCase
from django.db import models

from adv_company.models import AdvCompany
from service.models import Service
from .helpers.helpers_model import ModelTest, FieldBoolModelTest, FieldVerboseNameModelTest, FieldDigitsModelTest


class TestModelAdvCompany(ModelTest):
    model = AdvCompany

    @pytest.mark.django_db
    def test_has_all_attributes(self, instance):
        assert hasattr(instance, 'name')
        assert hasattr(instance, 'service')
        assert hasattr(instance, 'promotion_channel')
        assert hasattr(instance, 'budget')

        assert hasattr(instance, '__str__')

    @pytest.mark.django_db
    def test_str(self, instance):
        instance.name = 'Test_name'
        assert instance.__str__() == 'Test_name'
        assert isinstance(instance.__str__(), str)


class TestModelFieldName(FieldBoolModelTest, FieldVerboseNameModelTest, FieldDigitsModelTest):
    field_name = 'name'
    field_type = models.CharField
    model = AdvCompany
    unique = True
    verbose_name = 'Название компании'
    max_length = 255


class TestModelFieldService(FieldBoolModelTest, FieldVerboseNameModelTest):
    field_name = 'service'
    field_type = models.ManyToManyField
    model = AdvCompany
    verbose_name = 'Услуга'

    def test_relation_service(self):
        assert self.field.related_model == Service


class TestModelFieldPromotionChannel(FieldBoolModelTest, FieldVerboseNameModelTest, FieldDigitsModelTest):
    field_name = 'promotion_channel'
    field_type = models.CharField
    model = AdvCompany
    verbose_name = 'Канал продвижения'
    max_length = 127


class TestModelFieldBudget(FieldBoolModelTest, FieldVerboseNameModelTest, FieldDigitsModelTest):
    field_name = 'budget'
    field_type = models.DecimalField
    model = AdvCompany
    verbose_name = 'Бюджет'
    max_digits = 8
    decimal_places = 2
