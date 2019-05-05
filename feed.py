from feedgen.feed import FeedGenerator


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
