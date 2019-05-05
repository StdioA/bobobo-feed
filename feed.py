import xml.etree.ElementTree as ET
from feedgen.feed import FeedGenerator
from dateutil.parser import parse as dateparse


class BlogFeed:
    def __init__(self, updated_at):
        self.fg = FeedGenerator()
        self.fg.id("https://github.com/liuyubobobo/my-blog")
        self.fg.author({
            "name": "liuyubobobo",
            "email": "liuyubobobo@gmail.com"
        })
        self.fg.title("是不是很酷")
        self.fg.language("zh-CN")
        self.fg.updated(updated_at)

    def update(self, articles):
        """
        Add entry
        """
        for article in reversed(articles):
            fe = self.fg.add_entry()
            fe.id(article.rel_path)
            fe.title(article.title)
            fe.link(href=article.link)
            fe.content(article.html)
            fe.updated(updated=article.updated_at)

    def save(self, path):
        self.fg.atom_file(path)

    @classmethod
    def get_atom_update_time(cls, path):
        tree = ET.parse(path)
        try:
            updated = tree.findall(
                "{http://www.w3.org/2005/Atom}updated")[0].text
        except IndexError:
            return None
        return dateparse(updated)
