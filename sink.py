import dataclasses
from enum import Enum
from typing import Iterable, Literal

ArticleType = Literal["news", "opinion", "review"]


class ArticleType2(str, Enum):
    NEWS = "news"
    OPINION = "opinion"
    REVIEW = "review"


@dataclasses.dataclass
class Article:
    title: str
    body: str
    type: ArticleType2


# article1 = Article("title 1", "body 2", "news")
# article2 = Article("title 2", "body 2", "opinion")
# article3 = Article("title 3", "body 2", "review")

article1a = Article("title 1", "body 2", ArticleType2.NEWS)
article2a = Article("title 2", "body 2", ArticleType2.OPINION)
article3a = Article("title 3", "body 2", ArticleType2.REVIEW)


def my_function(articles: Iterable[Article]):
    pass


# my_function((article1, article2, article3))
my_function((article1a, article2a, article3a))
