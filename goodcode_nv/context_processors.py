def add_fortune(request):
    #adds my fortune template context
    from models import Fortune
    return {
	'fortune': Fortune.objects.filter(active=True).order_by('?')[0]
    }

