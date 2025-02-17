from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:  # If field is empty
            try:
                qs = self.model.objects.all()  # Query all objects of the model
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)  # Filter based on `for_fields`

                last_item = qs.order_by(self.attname).last()  # Get last item
                value = getattr(last_item, self.attname) + 1 if last_item else 0
            except ObjectDoesNotExist:
                value = 0  # Default to 0 if no objects exist

            setattr(model_instance, self.attname, value)  # Set new value
            return value
        else:
            return super().pre_save(model_instance, add)
