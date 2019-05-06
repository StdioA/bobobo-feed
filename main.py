import os
import constants
from repos import GitRepo
from blog_parser import BlogParser
from feed import BlogFeed


def main():
    print("Updating blog repo")
    blog_repo = GitRepo(force=True, **constants.BLOG_CONF)
    print("Updating atom repo")
    atom_repo = GitRepo(force=True, **constants.ATOM_CONF)

    parser = BlogParser(blog_repo.path)
    articles = parser.articles()
    committed_at = blog_repo.last_committed_at
    atom_path = os.path.join(atom_repo.path, "atom.xml")
    atom_updated = BlogFeed.get_atom_update_time(atom_path)
    if committed_at == atom_updated:
        print("Atom feed is up to date, exit.")
        return

    print("Generating atom.xml")
    feed = BlogFeed(committed_at)
    feed.update(articles[:50])
    feed.save(atom_path)

    if atom_repo.repo.is_dirty():
        print("Commit & push feed repo")
        atom_repo.commit_all()
        atom_repo.push()
    print("Done!")


if __name__ == "__main__":
    main()
