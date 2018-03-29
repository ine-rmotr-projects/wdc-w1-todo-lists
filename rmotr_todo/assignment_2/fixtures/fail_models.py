from unittest.mock import MagicMock

Item = MagicMock()

List = MagicMock()
List.__contains__ = MagicMock(return_value=False)
List.get_absolute_url = MagicMock(return_value='/')
