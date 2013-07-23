from django.views.generic.detail import DetailView

from faq.models import Topic, Question


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


def question_detail(request, topic_slug, slug):
    """
    A detail view of a Question.

    Templates:
        :template:`faq/question_detail.html`
    Context:
        question
            A :model:`faq.Question`.
        topic
            The :model:`faq.Topic` object related to ``question``.

    """
    extra_context = {
        'topic': Topic.objects.published().get(slug=topic_slug),
    }

    object_detail = ObjectDetailView.as_view(queryset=Question.objects.published(),
        extra_context=extra_context, context_object_name='question',
        slug_url_kwarg=slug)
    return object_detail(request)
