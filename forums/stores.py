class MembersStore:
	members = []
	last_id = 1

	def add(self, member):		
		member.id = MembersStore.last_id
		MembersStore.members.append(member)
		MembersStore.last_id += 1

	def get_all(self):
		return MembersStore.members

	def get_by_id(self, id):

		all_members = self.get_all()

		for member in all_members:
			if member.id == id:
				return member 
		return None

	def entity_exists(self, member):

		if self.get_by_id(member.id) is None:
			return False
		return True

	def delete(self, id):
		all_members = self.get_all()
		member_to_delete = self.get_by_id(id)

		all_members.remove(member_to_delete)

	def update(self, member, new_name, new_age):
		all_members = self.get_all()
		for member in all_members:
			member.name = new_name
			member.age = new_age

	def get_by_name(self, name):
		return (member for member in self.get_all() if member.name == member_name)

class PostsStore:
	posts = []

	def add(self, post):
		PostsStore.posts.append(post)

	def get_all(self):
		return PostsStore.posts

	def update(self, post, new_post_title, new_post_subject):
		all_posts = self.get_all()
		for post in all_posts:
			post.title = new_post_title
			post.subject = new_post_subject