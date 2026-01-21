bros = ('Deverton', 'Neldy')
sisters = ('Delicia', 'Kelsy')
siblings = bros + sisters
siblings = list(siblings)
siblings.insert(0, 'Antonio')
siblings.insert(1, 'Odete')
family_members = siblings
print(family_members)

#unpacking family members
parents = ()
family_members[0], family_members[1] = parents
#parents = family_members[0:2]
siblings = family_members[2:]
print(parents)
print(siblings)

