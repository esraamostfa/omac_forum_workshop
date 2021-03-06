import datetime

class Member:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.id = 0
		self.posts = []

	def __str__(self):
		return f"Name: {self.name}, Age: {self.age}"


class Post:
	def __init__(self, title, subject, member_id=0):
		self.title = title
		self.subject = subject
		self.id = 0
		self.member_id = member_id
		self.date = datetime.datetime.now()

	def __str__(self):
		return f"{self.title}: {self.subject}"