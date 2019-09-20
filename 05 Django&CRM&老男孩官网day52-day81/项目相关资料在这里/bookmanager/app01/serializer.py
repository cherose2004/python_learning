from rest_framework import serializers
from app01 import models


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


# def validate_title(value):
#     if 'mjj' in value:
#         raise serializers.ValidationError

#
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(validators=[])
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     pub_date = serializers.DateTimeField()
#
#     pub = PublisherSerializer(required=False, read_only=True)
#     authors = serializers.SerializerMethodField(read_only=True)  # get_字段名
#
#     post_pub = serializers.IntegerField(write_only=True)
#     post_author = serializers.ListField(write_only=True)
#
#     def validate_title(self, value):
#         if 'mjj' in value:
#             raise serializers.ValidationError
#         return value
#
#     def validate(self, attrs):
#         return attrs
#
#     def get_authors(self, obj):
#         ser_obj = AuthorSerializer(obj.authors.all(), many=True)
#         return ser_obj.data
#
#     def create(self, validated_data):
#         book_obj = models.Book.objects.create(
#             title=validated_data['title'],
#             price=validated_data['price'],
#             pub_date=validated_data['pub_date'],
#             pub_id=validated_data['post_pub']
#         )
#         book_obj.authors.set(validated_data['post_author'])
#         return book_obj
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.price = validated_data.get('price', instance.price)
#         instance.pub_date = validated_data.get('pub_date', instance.pub_date)
#         instance.pub_id = validated_data.get('post_pub', instance.pub_id)
#         instance.save()
#         instance.authors.set(validated_data.get('post_authors', instance.authors.all()))
#         return instance


class BookSerializer(serializers.ModelSerializer):
    pub_info = serializers.SerializerMethodField(read_only=True)
    authors_info = serializers.SerializerMethodField(read_only=True)

    def get_pub_info(self, obj):
        return PublisherSerializer(obj.pub).data

    def get_authors_info(self, obj):
        return AuthorSerializer(obj.authors.all(), many=True).data

    class Meta:
        model = models.Book
        fields = "__all__"
        # depth = 1
        extra_kwargs = {
            'pub': {'write_only': True},
            'authors': {'write_only': True},
        }
