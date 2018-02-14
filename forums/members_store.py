class MembersStore:
	members = []

	def add(member):
		MembersStore.members.append(member)

	def get_all():
		return MembersStore.members