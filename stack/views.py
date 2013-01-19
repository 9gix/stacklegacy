import json
from django.http import HttpResponse
from stack.models import App, AppStack, Architecture
from stack.forms import AppForm
from django.views.generic.detail import SingleObjectMixin, SingleObjectTemplateResponseMixin, BaseDetailView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(
            self.convert_context_to_json(context),
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

class StackListView(ListView):
    model = App

    def get_context_data(self, **kwargs):
        context = super(StackListView, self).get_context_data(**kwargs)
        context["app_meta"] = App._meta
        return context


class StackDetailView(DetailView):
    model = App

class StackCreate(CreateView):
    model = App
    form_class = AppForm

    def get_context_data(self, **kwargs):
        context = super(StackCreate, self).get_context_data(**kwargs)
        context["app_stack_meta"] = AppStack._meta
        context["architecture_meta"] = Architecture._meta
        return context

class StackUpdate(UpdateView):
    model = App
    form_class = AppForm

    def get_context_data(self, **kwargs):
        context = super(StackUpdate, self).get_context_data(**kwargs)
        context["app_stack_meta"] = AppStack._meta
        context["architecture_meta"] = Architecture._meta
        return context

class StackDelete(DeleteView):
    model = App
