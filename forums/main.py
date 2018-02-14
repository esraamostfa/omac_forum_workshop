import models
import members_store
import posts_store

member1 = models.Member("Mohamad", 23)
member2 = models.Member("Ahmad", 25)

post1 = models.Post("post 1", "this is post 1")
post2 = models.Post("post 2", "this is post 2")
post3 = models.Post("post 3", "this is post 3")

members_store.MembersStore.add(member1)
members_store.MembersStore.add(member2)

posts_store.PostsStore.add(post1)
posts_store.PostsStore.add(post2)
posts_store.PostsStore.add(post3)

posts_store.PostsStore.get_all()
members_store.MembersStore.get_all()