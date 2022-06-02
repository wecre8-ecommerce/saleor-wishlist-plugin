import graphene

from saleor.graphql.core.types.common import Error
from wishlist.graphql import enums

WishlistErrorCode = graphene.Enum.from_enum(enums.WishlistErrorCode)


class WishlistError(Error):
    code = WishlistErrorCode(description="The error code.", required=True)
