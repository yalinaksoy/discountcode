import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from billogram.api.models import DiscountCode


@login_required
def create_view(request):
    brand = int(request.GET.get('brand'))
    # check if brand is available and valid
    # return bad request if not
    # should use search brands service mentioned
    count = int(request.GET.get('count', 1))
    if count > 2000:
        return HttpResponse("Too many codes to create as a batch", status=400)
    percentage = float(request.GET.get('percentage', 10))
    if percentage > 100:
        return HttpResponse("Percentage is greater than the total price", status=400)
    response = DiscountCode.create_discount_codes(brand_id=brand,
                                                  discount_percent=percentage,
                                                  code_count=count)
    if response:
        # valid response
        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        # problem with response
        return HttpResponse("Service unavailable", status=503)


@login_required
def get_view(request):
    user = request.user
    brand = int(request.GET.get('brand'))
    # check if brand is available and valid
    # return bad request if not
    # should use search brands service mentioned
    response = DiscountCode.get_discount_code(user=user, brand_id=brand)
    if response:
        # valid response
        return HttpResponse(json.dumps(response.to_dict()), content_type="application/json")
    else:
        # problem with response
        return HttpResponse("Service unavailable", status=503)
