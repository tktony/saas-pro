from django.shortcuts import render

from subscriptions.models import SubscriptionPrice

# Create your views here.
def subscription_price_view(request, interval="month"):
    qs = SubscriptionPrice.objects.filter(featured=True)
    monthly_qs = qs.filter(interval=SubscriptionPrice.IntervalChoices.MONTHLY)
    year_qs = qs.filter(interval=SubscriptionPrice.IntervalChoices.YEARLY)

    #  🔍 Debugging output 
    # print("Total featured subscriptions:", qs.count())  
    # print("Monthly subscriptions count:", monthly_qs.count())  
    # for obj in monthly_qs:
    #     print(f"Subscription: {obj.subscription.name} - {obj.price}")  # Use `obj.subscription.name``
    #     print(obj)  # Check what objects exist in the queryset

    return render(request, "subscriptions/pricing.html", {
        "monthly_qs": monthly_qs,
        "yearly_qs": year_qs,
    })