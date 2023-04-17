from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def check_overlap(request):
    try:

      if request.method == 'POST':
          data = request.POST.dict()
          date_range_1 = {
            'start_date': data['date_1[start_date]'],
            'end_date': data['date_1[end_date]']
                          }
          date_range_2 = {
            'start_date': data['date_2[start_date]'],
            'end_date': data['date_2[end_date]']
                          }
          start_date_1 = datetime.strptime(date_range_1['start_date'], '%Y-%m-%d').date()
          end_date_1 = datetime.strptime(date_range_1['end_date'], '%Y-%m-%d').date()
          start_date_2 = datetime.strptime(date_range_2['start_date'], '%Y-%m-%d').date()
          end_date_2 = datetime.strptime(date_range_2['end_date'], '%Y-%m-%d').date()
          if end_date_1 < start_date_1 or end_date_2 < start_date_2:
              return HttpResponse("end date cannot be less than start date")
          elif end_date_1 < start_date_2 or end_date_2 < start_date_1:
                return JsonResponse(
                {
              "status": "no overlap",
              "message": "The two date ranges do not overlap."
                 })
          else :
              return JsonResponse(
               {
                "status": "overlap",
                "message": "The two date ranges overlap."
                })
    except: 
       return JsonResponse(
            {
                "Error": "Make sure the date format is correct",
                "message": "Usage Example: curl -X POST -d 'date_1[start_date]=2022-01-01&date_1[end_date]=2022-01-13&date_2[start_date]=2022-01-18&date_2[end_date]=2022-28' http://127.0.0.1:8000/date/"
            })
