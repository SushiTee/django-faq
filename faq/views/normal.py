from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.detail import DetailView

from faq.models import Topic, Question
from faq.views.shallow import _fragmentify


class ObjectDetailView(DetailView):
    extra_context = None
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if self.extra_context is not None:
            for key, value in self.extra_context.items():
                if callable(value):
                    context[key] = value()
                else:
                    context[key] = value
        return context


def topic_detail(request, slug):
    """
    A detail view of a Topic

    Templates:
        ``<topic_template_name>``
            If the :model:`faq.Topic` object has a ``template_name`` value,
            the system will attempt to load that template.
        :template:`faq/topic_detail.html`
            If there is no ``template_name`` given or the template specified
            does not exist the standard template will be used.
    Context:
        topic
            An :model:`faq.Topic` object.
        question_list
            A list of all published :model:`faq.Question` objects that relate
            to the given :model:`faq.Topic`.

    """
    extra_context = {
        'question_list': Question.objects.published().filter(topic__slug=slug),
    }

    object_detail = ObjectDetailView.as_view(queryset=Topic.objects.published(),
        extra_context=extra_context, context_object_name='question',
        slug_url_kwarg=slug, template_name='template_name')
    return object_detail(request)


def question_detail(request, topic_slug, slug):
    """
    A detail view of a Question.

    Simply redirects to a detail page for the related :model:`faq.Topic`
    (:view:`faq.views.topic_detail`) with the addition of a fragment
    identifier that links to the given :model:`faq.Question`.
    E.g. ``/faq/topic-slug/#question-slug``.

    """
    url = reverse('faq-topic-detail', kwargs={'slug': topic_slug})
    return _fragmentify(Question, slug, url)
