from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import InputForm
from .like.like import AutoLiker


class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InputForm()
        return context


class ResultView(TemplateView):
    template_name = 'app/result.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = InputForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data

            autoliker = AutoLiker(username=d['username'], password=d['password'], hashtag=d['hashtag'], max_like_count=d['max_like_count'], headless=False)
            autoliker.start()

            context['result'] = autoliker.get_result()

        return self.render_to_response(context)
