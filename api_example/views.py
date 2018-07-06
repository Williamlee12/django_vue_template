from django.http import JsonResponse
def names(request):
    return JsonResponse({'names': ['William', 'Rod', 'Grant']})
