from django import forms
from todo.models import Item

EMPTY_ITEM_ERROR = "Blank list items are not permitted"


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {'text':
                   forms.fields.TextInput(attrs={'placeholder':
                                                 'Enter a to-do item.'})}
        error_messages = {'text': {'required': EMPTY_ITEM_ERROR}}

    def save(self, list_):
        self.instance.list = list_
        return super().save()
