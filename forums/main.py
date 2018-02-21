import models
import stores

#----------------------define functions for tests-------------------

def creat_members():

	member1 = models.Member("Mohammad", 23)
	member2 = models.Member("Ahmad", 25)
	member3 = models.Member("Mohammad", 21)
	print(member1)
	print(member2)
	print(member3)
	print("=" * 30)

	return member1, member2, member3

def creat_posts():

	post1 = models.Post("post 1", "this is post 1", 1)
	post2 = models.Post("post 2", "this is post 2", 2)
	post3 = models.Post("post 3", "this is post 3", 3)
	post4 = models.Post("post 4", "this is post 4", 3)
	post5 = models.Post("post 5", "this is post 5", 1)
	post6 = models.Post("post 6", "this is post 6", 3)
	print(post1)
	print(post2)
	print(post3)
	print("=" * 30)

	return post1, post2, post3, post4, post5, post6 

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

def update_member(members_store, member):
    member_copy = models.Member(member.name, member.age)
    member_copy.id = member.id

    if member_copy is not member:
        print("member and member_copy are not the same !")

    print(member_copy)
    member_copy.name = "Mazen"
    members_store.update(member_copy)
    print(member_copy.name)
    print(member)
    print_all_members(members_store)
	
def get_member_by_name(members_store, name):	
	print(members_store.get_by_name(name))
	print("=" * 30)

def print_members_with_posts(members_store):
	members_with_posts = members_store.get_members_with_posts(posts_store.get_all())

	for member_with_posts in members_with_posts:
		print(f"{member_with_posts} has posts:")
		for post in member_with_posts.posts:
			print(f"\t{post}")

	print("=" * 30)

def print_top_two(members_store):
	print(members_store.get_top_two())
	print("=" * 30)

#--------------------------call functions for tests------------------------

members_store = stores.MembersStore()
posts_store = stores.PostsStore()
member_instances = creat_members()
member1, member2, member3 = member_instances
post_instances = creat_posts()
post1, post2, post3, post4, post5, post6 = post_instances

add_members_to_store(member_instances, members_store)
add_posts_to_store(post_instances, posts_store)
print_all_members(members_store)
get_member_by_id(members_store, 1)
delete_member(members_store, member2)
update_member(members_store ,member3)
get_member_by_name(members_store, "Mohammad")
print_members_with_posts(members_store)
print_top_two(members_store)