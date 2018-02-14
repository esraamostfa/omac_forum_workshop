class MembersStore:
	members = []

	def add(self, member):
		MembersStore.members.append(member)

	def get_all(self):
		return MembersStore.members


class PostsStore:
	posts = []

	def add(self, post):
		PostsStore.posts.append(post)

	def get_all(self):
		return PostsStore.posts