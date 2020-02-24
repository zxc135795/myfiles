# ProjectName:Ldemo002
# FileName:search_indexes
# author:asus
# datetime:2020/2/24 9:20
# software: PyCharm
from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
