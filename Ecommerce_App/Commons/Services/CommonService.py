


from django.utils.text import slugify




def generate_unique_slug(instance,model, new_slug=None):
    slug = None
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)
    qs = model.objects.filter(slug=slug)
    if qs.exists():
        new_slug = f"{slug}-{qs.count()}"
        return generate_unique_slug(instance, new_slug=new_slug)
    return slug