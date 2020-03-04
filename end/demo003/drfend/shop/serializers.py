# ProjectName:Ldemo003
# FileName:serializers
# author:asus
# datetime:2020/2/26 15:41
# software: PyCharm
from rest_framework import serializers
from .models import *


class CategorySerizlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(label='分类名称')

    def create(self, validated_data):
        instace = Category.objects.create(**validated_data)
        return instace

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class GoodSerizlizer(serializers.Serializer):
    """
    自定义序列化方法 继承serializer的父类Serializer
    序列化的字段 exp： name
    重写序列化方法 def create ，update ，...
    """
    name = serializers.CharField(label='商品名称')
    category = CategorySerizlizer(label='分类')

    def validate_category(self, category):
        """
        处理验证category数据
        :param category: 原始值 被处理
        :return: 返回值 已处理
        """
        try:
            Category.objects.get(name=category['name'])
        except:
            raise serializers.ValidationError('分类不存在')
        return category

    def validate(self, attrs):
        """
        验证数据
        :param attrs:收到数据
        :return:更改后数据
        """
        try:
            # 数据正确处理
            c = Category.objects.get(name=attrs['category']['name'])
        except:
            # 数据不匹配处理
            c = Category.objects.create(name=attrs['category']['name'])
        # 更改原始数据 返回需要数据
        attrs['category'] = c
        return attrs

    def create(self, validated_data):
        """
        重写create方法 自定义序列化方法
        :param validated_data: 接收到的原始数据
        :return: 返回序列化后的数据
        """
        instance = Good.objects.create(**validated_data)
        return instance


# class CustomSerializer(serializers.ReadOnlyField):
#     def get

class CategorySerizlizer1(serializers.ModelSerializer):
    # read_only 属性 True 只读 False 可读写
    goods = serializers.StringRelatedField(many=True, read_only=True)

    # goods = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'goods')


class GoodSerizlizer1(serializers.ModelSerializer):
    """
    使用模板result自带序列化方法
    """
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)

    class Meta:
        model = Good
        fields = ('id', 'name', 'docs', 'price', 'category_id', 'category_name')


class GoodImgsSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    # def validate_good(self, data):
    #     print("原始值",data)
    #     try:
    #         g = Good.objects.get(name = data)
    #         print(g,type(g),"+++")
    #         return g
    #     except:
    #         raise serializers.ValidationError("输入的商品不存在")
    #     # return data

    def validate(self, attrs):
        print("原始值", attrs["good"]["name"])
        try:
            g = Good.objects.get(name=attrs["good"]["name"])
            print("修改商品", g)
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品不存在")
        return attrs

    def create(self, validated_data):
        print(validated_data)
        instance = GoodImgs.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.img = validated_data.get("img", instance.img)
        instance.good = validated_data.get("good", instance.good)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["user_permissions", "groups"]

    def validate(self, attrs):
        print("原生创建")
        from django.contrib.auth import hashers
        if attrs.get("password"):
            attrs["password"] = hashers.make_password(attrs["password"])
        print("修改之后的字段")
        return attrs


class UserRegistSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10, min_length=3, error_messages={
        "required": "用户名必填"
    })
    password = serializers.CharField(max_length=10, min_length=3, write_only=True)
    password2 = serializers.CharField(max_length=10, min_length=3, write_only=True)

    def validate_password2(self, data):
        if data != self.initial_data["password"]:
            raise serializers.ValidationError("密码不一致")
        else:
            return data

    def create(self, validated_data):
        print("提交数据", validated_data)
        return User.objects.create_user(username=validated_data.get("username"), email=validated_data.get("email"),
                                        password=validated_data.get("password"))


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
