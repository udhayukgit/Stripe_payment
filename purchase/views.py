from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import stripe
from json_response import JsonResponse

def index(request):
	template = loader.get_template('products.html')
	context = {}
	return HttpResponse(template.render(context, request))
    

def make_charge_stripe(request,amount):

	stripe.api_key = "sk_test_51ILuAEFeeXLUQ8Xl8mGNHWcVsIEBDwNZj2k6aeTQmGn9Aby1bEW4ZmGmLDlaxTtoraU94txbnNKbversueUK5D8P00pX8pmUvB"

	#`source` is obtained with Stripe.js; see https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token
	stripe_payment = stripe.Charge.create(
	  amount=amount,
	  currency="inr",
	  source="tok_amex",
	  description="Make a Charge in stripe",
	)
	
	message = "successfull payment!."
	return JsonResponse({'status':'true','message':stripe_payment}, status=200)

