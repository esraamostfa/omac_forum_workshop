import stores
import data
from flask import Flask

app = Flask(__name__)

members_store = stores.MembersStore()
posts_store = stores.PostsStore()

from views import *

if __name__  == "__main__":
    data.seed_stores(members_store, posts_store)
    app.run()