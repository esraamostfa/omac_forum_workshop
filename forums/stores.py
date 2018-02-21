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

	def update(self, member):
		all_members = self.get_all()

		return [member if current_member.id == member.id else current_member for current_member in all_members]

	def get_by_name(self, name):
		return (member for member in self.get_all() if member.name == name)

class PostsStore:
	posts = []
	last_id = 1

	def add(self, post):
		post.id = PostsStore.last_id
		PostsStore.posts.append(post)
		PostsStore.last_id += 1

	def get_all(self):
		return PostsStore.posts

	def update(self, post):
		all_posts = self.get_all()

		return [post if current_post.id == post.id else current_post for current_post in all_posts]
		