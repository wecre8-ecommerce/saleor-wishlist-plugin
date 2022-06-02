from saleor.graphql.views import GraphQLView

from saleor.plugins.base_plugin import BasePlugin
from wishlist.graphql.schema import schema


class WishlistPlugin(BasePlugin):
    PLUGIN_ID = "wishlist"
    PLUGIN_NAME = "wishlist"
    DEFAULT_ACTIVE = True
    CONFIGURATION_PER_CHANNEL = False

    def webhook(self, request, path, previous_value):
        view = GraphQLView.as_view(schema=schema)
        request.app = self
        return view(request)
