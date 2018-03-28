from unittest.mock import MagicMock

Item = MagicMock()
Item.objects = MagicMock()
Item.objects.count = MagicMock(return_value=0)
Item.objects.create = MagicMock(return_value=None)
