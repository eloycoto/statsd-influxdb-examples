from django.core.urlresolvers import resolve
from statsd.defaults.env import statsd

class Statsd(object):

    def process_request(self, request):
        self.current_view = resolve(request.path).url_name
        statsd.incr("view.exceptions.{0}".format(self.current_view))
        self.timer = statsd.timer('view.{0}'.format(self.current_view))
        self.timer.start()

    def process_response(self, request, response):
        self.timer.stop()
        return response

    def process_exception(self, request, exception):
        self.timer.stop()
        statsd.incr("view.exceptions.{0}".format(self.current_view))

