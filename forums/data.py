import models
import stores

posts_store = stores.PostsStore()
posts_store.add(models.Post("Life", "Life is alawys great", 1))
posts_store.add(models.Post("Sunshine", "Sunshine is amazing", 2))