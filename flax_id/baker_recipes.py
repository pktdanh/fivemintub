from flax_id import get_flax_id
from model_bakery import baker

baker.generators.add("flax_id.django.fields.FlaxId", get_flax_id)
