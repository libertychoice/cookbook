from cookbook.models import CategoryMain


def categories_processor(request):
    categories = CategoryMain.objects.all()
    return {'categories': categories}
