bros = ('Deverton', 'Neldy')
sisters = ('Delicia', 'Kelsy')
siblings = bros + sisters
siblings = list(siblings)
siblings.insert(0, 'Antonio')
siblings.insert(1, 'Odete')
family_members = siblings


print(family_members[-4:-1])


['Antonio', 'Odete', 'Deverton', 'Neldy', 'Delicia', 'Kelsy']
#   0          1            2       3           4           5  da esq pr direita)
#                                              -2           -1
#unpacking family members
parents = ()
#family_members[0], family_members[1] = parents
#parents = family_members[0:2]
siblings = family_members[2:]
#print(parents)
#print(siblings)

