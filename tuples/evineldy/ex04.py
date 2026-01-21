bros = ('Deverton', 'Neldy')

sisters = ('Delicia', 'Kelsy')
siblings = bros + sisters
siblings = list(siblings)
siblings.insert(0, 'Antonio')
siblings.insert(1, 'Odete')
family_members = siblings
family_members = tuple(family_members)
print(type(family_members))
print(family_members[3])


bros = family_members
print(bros)
