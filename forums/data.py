import models


members_data = [
    models.Member("Mohammed", 20),
    models.Member("Mohammed", 22),
    models.Member("Abdo", 25),
]

posts_data = [
    models.Post("Agriculture", "Agriculture is amazing", members_data[0].id),
    models.Post("Engineering", "I love engineering", members_data[0].id),

    models.Post("Medicine", "Medicine is great", members_data[1].id),
    models.Post("Architecture", "Spectacular art", members_data[1].id),
    models.Post("Astronomy", "Space is awesome", members_data[1].id),

    models.Post("Geology", "Earth is our friend", members_data[2].id),
    models.Post("ComputerSci", "Our passion", members_data[2].id),
    models.Post("Algorithms", "Yeah, more of that", members_data[2].id),
    models.Post("Operating Systems", "Ewww", members_data[2].id),
]

def seed_stores(members_store, posts_store):
    for member in members_data:
        members_store.add(member)

    for post in posts_data:
        posts_store.add(post)
