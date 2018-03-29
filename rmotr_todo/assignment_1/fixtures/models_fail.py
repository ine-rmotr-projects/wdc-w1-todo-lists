from test_utils.mocked_models import Item


class ItemNoCount(Item):

    def _count(cls):
        return 0
