from itertools import product

class BaseStore:
	def __init__(self, data_provider, last_id):
		self._data_provider = data_provider
		self._last_id = last_id

	def add(self, instance):		
		instance.id = self.last_id
		self._data_provider.append(instance)
		self._last_id += 1

	def get_all(self):
		return self._data_provider

	def get_by_id(self, id):

		all_instances = self.get_all()

		for instance in all_instances:
			if instance.id == id:
				return instance 
		return None

	def delete(self, id):
		all_instances = self.get_all()
		instance_to_delete = self.get_by_id(id)

		all_instances.remove(instance_to_delete)

	def entity_exists(self, instance):

		if self.get_by_id(instance.id) is None:
			return False
		return True

	def update(self, instance):
		all_instances = self.get_all()
		for i, current_instance in enumerate(all_instances):
			if instance.id == current_instance.id:
				all_instances[i] = instance
				break

		return instance
			

class MembersStore(BaseStore):
	members = []
	last_id = 1

	def __init__(self):
		super().__init__(MembersStore.members, MembersStore.last_id)

	def get_by_name(self, name):
		return (member for member in self.get_all() if member.name == name)

	def get_members_with_posts(self, all_posts):
		all_members = self.get_all()

		for post, member in product(all_posts, all_members):
			if post.member_id == member.id:
				member.posts.append(post)

		return (member for member in all_members)


	def get_top_two(self):
		all_members_with_posts = self.get_members_with_posts(PostsStore.posts)
		sorted_members = sorted(all_members_with_posts, key = lambda member: len(member.posts), reverse=True)

		return sorted_members[:2]

class PostsStore(BaseStore):
	posts = []
	last_id = 1

	def __init__(self):
		super().__init__(PostsStore.posts, PostsStore.last_id)

	def get_posts_by_date(self):
		all_posts = self.get_all()
		all_posts.sort(key =lambda post: post.date , reverse = True)

		return (post for post in all_posts)