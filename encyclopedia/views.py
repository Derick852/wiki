from django.shortcuts import render

from . import util
import random, markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    if f"{title}" == "new":
        return render(request, "encyclopedia/new.html")
    elif f"{title}" == "ran":
        entries = util.list_entries()
        ran = random.choice(entries)
        return render(request, "encyclopedia/entry.html", {
            "content" : markdown.markdown(util.get_entry(ran)),
            "title"   : ran,
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "content" : markdown.markdown(util.get_entry(f"{title}")),
            "title"   : f"{title}"
            })
