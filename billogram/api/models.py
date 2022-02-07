import uuid
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class DiscountCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    redeemed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    discount_percent = models.IntegerField(default=10)
    code_string = models.TextField(default=uuid.uuid4())
    brand_id = models.IntegerField()

    @classmethod
    def create_discount_codes(cls, brand_id, discount_percent=10, code_count=1):
        """
        Function to create function codes for a brand
        :param brand_id: id of brand which discount code belongs to
        :param discount_percent: percentage of the discount code, 10 percent default
        :param code_count : number of codes to be created, 1 code default
        """
        try:
            for _ in range(code_count):
                cls.objects.create(brand_id=brand_id,
                                   discount_percent=discount_percent)
        except Exception as e:
            # this should be a logging system
            print("Database write error: {}".format(e))
            return False
        return True

    @classmethod
    def get_discount_code(cls, brand_id, user):
        """
        Function to get discount codes for a user
        :param brand_id: id of the brand user want to redeem coupon to
        :param user: user responsible from request
        """
        applicable_codes = cls.objects.filter(Q(brand_id=brand_id) & Q(redeemed=False) &
                                              Q(Q(user__isnull=True) | Q(user=user)))
        if applicable_codes.exists():
            curr_code = applicable_codes.first()
            curr_code.redeemed = True
            curr_code.user = user
            curr_code.save()
            return curr_code
        else:
            return False

    def to_dict(self):
        return {"brand": self.brand_id,
                "discount_code": self.code_string,
                "discount_percentage": self.discount_percent,
                "crated": self.created.strftime("%m/%d/%Y")
                }
