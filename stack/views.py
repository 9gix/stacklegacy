import json
from django.http import HttpResponse
from stack.models import App, AppStack
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

class StackCreate(CreateView):
    model = App

class StackUpdate(UpdateView):
    model = App

class StackDelete(DeleteView):
    model = App
