import graphene

from wishlist import models
from graphene_django.types import DjangoObjectType
from saleor.graphql.core.connection import CountableConnection

class CountableDjangoObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(cls, *args, **kwargs):
        # Force it to use the countable connection
        countable_conn = CountableConnection.create_type(
            "{}CountableConnection".format(cls.__name__), node=cls
        )
        super().__init_subclass_with_meta__(*args, connection=countable_conn, **kwargs)



class Wishlist(CountableDjangoObjectType):
    products = graphene.List(graphene.ID, description="List of products IDs.")
    slug_products = graphene.List(
        graphene.String, description="List of products slugs."
    )

    variants = graphene.List(graphene.ID, description="List of variants IDs.")

    class Meta:
        model = models.Wishlist
        filter_fields = [
            "id",
            "token",
        ]
        interfaces = (graphene.relay.Node,)
        exclude = ["user", "token"]

    def resolve_variants(root, info):
        return [
            graphene.Node.to_global_id("ProductVariant", id)
            for id in root.variants.values_list("id", flat=True)
        ]

    def resolve_products(root, info):
        return [
            graphene.Node.to_global_id("Product", id)
            for id in root.products.values_list("id", flat=True)
        ]

    def resolve_slug_products(root, info):
        return [(slug) for slug in root.products.values_list("slug", flat=True)]
