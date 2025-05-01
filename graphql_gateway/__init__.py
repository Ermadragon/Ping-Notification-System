from flask import Flask
from .schema import schema
from strawberry.flask.views import GraphQLView
from .auth import jwt_required_graphql

def create_app():
    app = Flask(__name__)

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql_view",
            schema=schema,
            graphiql=True,
            decorators=[jwt_required_graphql],
        ),
    )

    return app
