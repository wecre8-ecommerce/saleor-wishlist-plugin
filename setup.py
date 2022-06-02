from setuptools import setup

setup(
    name="wishlist",
    version="0.1.0",
    packages=["wishlist"],
    package_dir={"wishlist": "wishlist"},
    description="Wishlist integration",
    entry_points={
        "saleor.plugins": ["wishlist = wishlist.plugin:WishlistPlugin"],
    },
)