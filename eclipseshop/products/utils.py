from django.core.paginator import Paginator


def paginate_products(request, products, results):
    page = request.GET.get('page', 1)
    # results = 6
    paginator = Paginator(products, results, allow_empty_first_page=True)
    products = paginator.get_page(page)
    left_index = int(page) - 4
    right_index = int(page) + 5
    if left_index < 1:
        left_index = 1
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
    custom_range = range(left_index, right_index)
    return custom_range, products
