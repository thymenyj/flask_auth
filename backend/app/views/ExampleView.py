from flask.views import MethodView


class ExampleView(MethodView):

    def get(self):
        return {}
