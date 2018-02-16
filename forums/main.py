import models
import stores

member1 = models.Member("Mohamad", 23, id)
member2 = models.Member("Ahmad", 25, id)

post1 = models.Post("post 1", "this is post 1")
post2 = models.Post("post 2", "this is post 2")
post3 = models.Post("post 3", "this is post 3")

members_store = stores.MembersStore()
posts_store = stores.PostsStore()

members_store.add(member1)
members_store.add(member2)

posts_store.add(post1)
posts_store.add(post2)
posts_store.add(post3)

members_store.get_all()
posts_store.get_all()

members_store.get_by_id(1)
members_store.get_by_id(2)

print(members_store.entity_exists(member1))
print(members_store.entity_exists(member2))