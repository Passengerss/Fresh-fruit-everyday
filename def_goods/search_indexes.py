from haystack import indexes
from .models import GoodsInfo

class GoodsInfoIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return GoodsInfo
    # 检索  Goodsinfo 中所有内容，即商品表所有内容
    def index_queryset(self,using=None):
        return self.get_model().objects.all()