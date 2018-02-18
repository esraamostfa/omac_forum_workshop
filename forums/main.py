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

members_store.delete(2)
print(members_store.entity_exists(member2))

member1_copy = models.Member(member1.name, member1.age, member1.id)
members_store.update(member1_copy, 'Mazen', 21)
print(member1.name, member1.age)
print(member1_copy.name, member1_copy.age)

post1_copy = models.Post(post1.title, post1.subject)
posts_store.update(post1_copy, "post 1 copy", "this is post 1 copy")
print(post1.title + ":" , post1.subject)
print(post1_copy.title + ":", post1_copy.subject)