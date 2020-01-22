from django.views.generic.base import View
from exams.models import Examination


class ExamsListView(View):
    def get(self, request):
        """

        :param request:
        :return:
        """
        exams = Examination.objects.all()

        from django.core import serializers
        import json
        json_data = serializers.serialize('json', exams)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        return JsonResponse(json_data, safe=False)
