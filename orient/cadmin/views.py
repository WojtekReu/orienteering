from datetime import time
import logging
import csv
from django.contrib import admin
from django.views import generic
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
#from .forms import OrganizerForm, SeasonForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)

from django.core.urlresolvers import reverse
from .forms import LoadResultsForm, LoadRunnersForm
from cup.models import Runner, Result, Marathon, Route


class LoadRunnersFormView(generic.FormView):
    template_name = 'cadmin/runners_form.html'
    form_class = LoadRunnersForm

    def form_valid(self, form):
        """

        :param form:
        :return:
        """
        users_file = form.files['users_file']
        raw = users_file.read()
        data = raw.decode('utf-8')

        users = []
        is_process_data = False
        for line in data.split('\n'):
            if not is_process_data:
                # omit first line because it must be header
                is_process_data = True
                continue

            l = line.split(',')
            if len(l) > 5:
                users.append({
                    'first_name': l[3],
                    'last_name': l[2],
                    'gender': l[0],
                    'year': l[1],
                    'locality': l[4],
                    'phone': l[5],
                    'email': l[6],
                })

        runners_count = Runner.objects.all().count()
        count = 0
        for nr, user in enumerate(users):
            gender = None
            if user['gender'] == 'M':
                gender = Runner.GENDER_MALE
            elif user['gender'] == 'K':
                gender = Runner.GENDER_FEMALE
            runner = Runner.objects.create(
                first_name=user['first_name'],
                last_name=user['last_name'],
                username='userf_{}'.format(runners_count + nr),
                gender=gender,
                birth_year=user['year'],
                locality=user['locality'],
                phone=user['phone'],
                email=user['email'],
            )
            if runner:
                count += 1

        response = 'Created {}, Total num: {}'.format(count, runners_count)
        return HttpResponseRedirect(reverse('load_runners'))


class LoadResultsFormView(generic.FormView):
    template_name = 'cadmin/results_form.html'
    form_class = LoadResultsForm

    def form_valid(self, form):
        """

        :param form:
        :return:
        """
        results_file = form.files['results_file']
        marathon = Marathon.objects.get(pk=int(form.cleaned_data['marathon']))
        raw = results_file.read()
        data = raw.decode('utf-8')

        results = []
        is_process_data = False
        for line in data.split('\n'):
            if not is_process_data:
                # omit first line because it must be header
                is_process_data = True
                continue

            l = line.split(',')
            if len(l) > 5:
                results.append({
                    'result_pk': l[0],
                    'first_name': l[1],
                    'last_name': l[2],
                    'year': l[3],
                    'locality': l[4],
                    'route': l[5],
                    'r_number': int(l[6]),
                    'meta_time': time(*(int(i) for i in l[7].split(':'))),
                    'total_time': time(*(int(i) for i in l[8].split(':'))),
                    'pk_points': int(l[9]),
                    'penalty_points': int(l[10]),
                    'ranking': l[11],
                })

        for nr, result in enumerate(results):
            if result['result_pk']:
                result_obj = Result.objects.get(pk=result['result_pk'])
                # result_obj.route = result['route']  # TODO: get route from type
                result_obj.r_number = result['r_number']
                result_obj.meta_time = result['meta_time']
                result_obj.total_time = result['total_time']
                result_obj.pk_points = result['pk_points']
                result_obj.penalty_points = result['penalty_points']
                result_obj.ranking = result['ranking']  # TODO: prepare check ranking
            else:
                route = Route.objects.filter(
                    marathon=marathon,
                    category=result['route']
                )[0]
                runner = Runner.objects.filter(
                    first_name=result['first_name'],
                    last_name=result['last_name'],
                    birth_year=result['year'],
                    locality=result['locality']
                )[0]
                result_obj = Result.objects.create(
                    route=route,
                    runner=runner,
                    r_number=result['r_number'],
                )
            result_obj.save()

        response = 'Results Updated: {}'.format(len(results))
        return HttpResponseRedirect(reverse('load_results'))


class MarathonResults(generic.ListView):
    model = Result

    def get(self, request, *args, **kwargs):
        self.marathon_pk = None
        for arg in args:
            if isinstance(arg, dict):
                self.marathon_pk = arg['marathon_pk']
        if 'marathon_pk' in kwargs:
            self.marathon_pk = kwargs['marathon_pk']
        return super(MarathonResults, self).get(request, args, kwargs)

    def get_queryset(self):
        queryset = super(MarathonResults, self).get_queryset()
        return queryset.filter(route__marathon__pk=self.marathon_pk)

    def dispatch(self, request, *args, **kwargs):
        handle = super(MarathonResults, self).dispatch(request, args, kwargs)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename="user_results.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Number',
            'First Name',
            'Last Name',
            'Birth Year',
            'Locality',
            'Route',
            'Number',
            'Meta Time',
            'Total Time',
            'Points',
            'Penalty Points',
            'Ranking',
        ])
        for result in handle.context_data['result_list']:
            writer.writerow([
                result.pk,
                result.runner.first_name,
                result.runner.last_name,
                result.runner.birth_year,
                result.runner.locality,
                result.route.category,
                result.r_number,
                result.meta_time,
                result.total_time,
                result.pk_points,
                result.penalty_points,
                result.ranking,
            ])

        return response
