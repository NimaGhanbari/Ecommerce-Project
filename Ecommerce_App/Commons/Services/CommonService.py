
import random

from django.utils.text import slugify




def generate_unique_slug(instance,model, new_slug=None):
    # In this section, recursive functions are used instead of loops
    slug = None
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)
    qs = model.objects.filter(slug=slug)
    if qs.exists():
        new_slug = f"{slug}-{qs.count()}"
        return generate_unique_slug(instance,model, new_slug=new_slug)
    return slug



def generate_unique_unique_code(instance,model):
    # In this section, recursive functions are used instead of loops
    random_code = random.randint(1000,9999)
    qs = model.objects.filter(uniqe_code=random_code)
    if qs.exists():
        return generate_unique_slug(instance,model)
    return random_code