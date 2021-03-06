from decimal import Decimal
from django.test import TestCase
from . import models

class LotsModelsTestCase(TestCase):
    fixtures = ['fixture_lots.json']

    def setUp(self) -> None:
        self.currency = models.Currency.objects.last()
        self.lot = models.Lot.objects.last()

    def test_lot_str(self):
        self.assertEqual(self.lot.__str__(), 'Партия 875f551f')

    def test_lot_save(self):
        self.assertEqual(self.lot.lot_number, 'Партия 875f551f')

    def test_total_amount(self):
        self.lot.save()
        self.assertEqual(self.lot.total_amount(), Decimal('500000.00'))

    def test_currency_str(self):
        self.assertEqual(self.currency.__str__(), 'сум')
