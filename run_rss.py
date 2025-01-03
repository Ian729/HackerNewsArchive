import feedparser
from translate import Translator

T = Translator(to_lang="zh")
ents = feedparser.parse("https://news.ycombinator.com/rss").entries
hacker_news = ""
for ent in ents[:30]:
    hacker_news += "* "
    current = ent.get("title", "")
    hacker_news += current
    hacker_news += "\n"
    hacker_news += "* "
    trans = T.translate(current)
    hacker_news += trans
    hacker_news += "\n"
    hacker_news += "* "
    published = ent.get("published", "")
    hacker_news += published
    hacker_news += "\n"
    hacker_news += "* "
    link = ent.get("link", "")
    hacker_news += link
    hacker_news += "\n"
    hacker_news += "----\n"


md = open("./README.md", "w")
md.write("# HackerNewsArchive\n")
md.write("Auto HackerNews and Translate\n")
md.write("\n")
md.write("## HackerNews\n")
md.write(hacker_news)
md.write("\n")

print("Done!")
