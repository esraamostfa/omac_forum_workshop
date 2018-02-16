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

	def entity_exists(self, member):
		all_members = self.get_all()

		if member in all_members:
			return True
		return False

	def delete(self, id):
		all_members = self.get_all()
		member_to_delete = self.get_by_id(id)

		all_members.remove(member_to_delete)


class PostsStore:
	posts = []

	def add(self, post):
		PostsStore.posts.append(post)

	def get_all(self):
		return PostsStore.posts