import graphene
from graphene_django import DjangoObjectType

# class GroceryType(DjangoObjectType):
#     class Meta:
#         model = Grocery
#         fields = (
#             'product_tag',
#             'name',
#             'category',
#             'price',
#             'quantity',
#             'imageurl',
#             'status',
#             'date_created',
#         )

# class Query(graphene.ObjectType):
#     categories = graphene.List(CategoryType)
#     books = graphene.List(BookType)
#     groceries = graphene.List(GroceryType)

#     def resolve_books(root, info, **kwargs):
#         # Querying a list
#         return Book.objects.all()

#     def resolve_categories(root, info, **kwargs):
#         # Querying a list
#         return Category.objects.all()

#     def resolve_groceries(root, info, **kwargs):
#         # Querying a list
#         return Grocery.objects.all()

# schema = graphene.Schema(query=Query)