import models
import stores

#----------------------define functions for tests-------------------

def creat_members():

	member1 = models.Member("Mohammad", 23)
	member2 = models.Member("Ahmad", 25)
	member3 = models.Member("Mohammad", 21)
	print(member1)
	print(member2)
	print("=" * 30)

	return member1, member2

def creat_posts():

	post1 = models.Post("post 1", "this is post 1")
	post2 = models.Post("post 2", "this is post 2")
	post3 = models.Post("post 3", "this is post 3")
	print(post1)
	print(post2)
	print(post3)
	print("=" * 30)

	return post1, post2, post3

def add_members_to_store(member_instances, members_store):

	for member in member_instances:
		members_store.add(member)

def add_posts_to_store(post_instances, posts_store):

	for post in post_instances:
		posts_store.add(post)

def print_all_members(members_store):
	print(members_store.get_all())
	print("=" * 30)

def get_member_by_id(members_store, id):
	print(members_store.get_by_id(id))
	print("=" * 30)

def delete_member(members_store, member):
	members_store.delete(member.id)
	print(members_store.entity_exists(member))
	print("=" * 30)

def update_member(members_store ,member):
	members_store.update(member, 'Mazen', 21)
	print(member.name, member.age)
	print("=" * 30)

def update_post(posts_store, post):
	posts_store.update(post, "updated post", "this post is updated")
	print(post.title + ":" , post.subject)
	print("=" * 30)
	
def get_member_by_name(members_store, name):	
	print(members_store.get_by_name(name))

#--------------------------call functions for tests------------------------

members_store = stores.MembersStore()
posts_store = stores.PostsStore()
member_instances = creat_members()
member1, member2 = member_instances
post_instances = creat_posts()
post1, post2, post3 = post_instances

creat_members()
creat_posts()
add_members_to_store(member_instances, members_store)
add_posts_to_store(post_instances, posts_store)
print_all_members(members_store)
get_member_by_id(members_store, 1)
delete_member(members_store, member2)
update_member(members_store ,member1)
update_post(posts_store, post1)
get_member_by_name(members_store, "Mohammad")