import os
from blog_parser import BlogParser
from repos import blog_repo, atom_repo
from feed import BlogFeed


if __name__ == "__main__":
    parser = BlogParser(blog_repo.path)
    articles = parser.articles()
    committed_at = blog_repo.last_committed_at
    # TODO: Check whether feed should be regenerated

    atom_path = os.path.join(atom_repo.path, "atom.xml")
    feed = BlogFeed(committed_at)
    feed.update(articles[:50])
    feed.save(atom_path)

    # TODO: Commit & push feed repo
    # TODO: Manage configuration / constants
