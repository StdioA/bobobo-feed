import os
import re
from functools import reduce
from operator import attrgetter
from urllib.parse import urljoin
from markdown import markdown
import constants


class Article:
    date_re = re.compile(r"\d{4}-\d{1,2}-\d{1,2}")
    head_re = re.compile(r"\#+ ?(.+)")
    url_base = constants.BLOG_URL_BASE
    img_base = constants.BLOG_IMG_BASE

    def __init__(self, path):
        self.path = path
        self._content = None

    def __hash__(self):
        return hash((self.date, self.content))

    @property
    def rel_path(self):
        return self.path.replace("\\", "/").replace("my-blog/", "")

    @property
    def link(self):
        return urljoin(self.url_base, self.rel_path)

    @property
    def content(self):
        if self._content is None:
            self._content = open(self.path, encoding='utf-8').read()
        return self._content

    @property
    def html(self):
        content = self.content
        # Alter image links
        img_re = re.compile(r"\!\[.+\]\((.+)\)")
        images = img_re.finditer(content)
        for image in images:
            original_url = image.group(1)
            altered_url = reduce(urljoin, [self.img_base, self.rel_path,
                                           original_url])
            content = content.replace(
                "({})".format(original_url),
                "({})".format(altered_url))
        # Alter links
        url_re = re.compile(r"\[.+\]\((.+)\)")
        links = url_re.finditer(content)
        for link in links:
            original_url = link.group(1)
            altered_url = urljoin(self.link, original_url)
            content = content.replace(
                "({})".format(original_url),
                "({})".format(altered_url))

        html = markdown(content)
        return html

    @property
    def date(self):
        return self.date_re.findall(self.path)[0]

    @property
    def updated_at(self):
        return "{}T00:00:00-0700".format(self.date)

    @property
    def title(self):
        try:
            return next(self.head_re.finditer(self.content)).group(1)
        except StopIteration:
            return "{} - 无题".format(self.date)


class BlogParser:
    article_re = re.compile(r"\d{4}-\d{1,2}-\d{1,2}")

    def __init__(self, path):
        self.path = path

    def articles(self):
        # Find all articles
        articles = []
        for root, _, files in os.walk(self.path):
            for file in files:
                if self.article_re.search(root) and file == "readme.md":
                    article_path = os.path.join(root, file)
                    articles.append(Article(article_path))
        articles.sort(key=attrgetter("date"), reverse=True)
        return articles


if __name__ == "__main__":
    feed = BlogParser("my-blog")
    articles = feed.articles()
    for a in articles:
        print(a.date, a.title)
