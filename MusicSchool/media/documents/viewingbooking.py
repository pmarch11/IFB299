def confirm_booking(request):
	template = 'bookingconfirmation.html'
	context = {'booking': bookingModel.objects.order_by('bookingID')[0], 'bookingRecurring': bookingModelRecurring.objects.order_by('bookingID')[0]}
	return render_to_response(template, context)