class PostsStore:
	posts = []

	def add(post):
		PostsStore.posts.append(post)

	def get_all():
		return PostsStore.posts 