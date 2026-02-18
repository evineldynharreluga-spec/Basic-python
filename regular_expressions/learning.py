import re


''''txt = 'I love to teach Python and Javascript'
match = re.match('I love to teach', txt, re.I)
print(match)

#primeira e ultima posicao do match
span = match.span()
print(span)

start, end = span
print(start, end)
substring = txt[start:end]
print(substring)'''

''''txt = 'I love to code'
match = re.search('oe', txt, re.I)
print(match)

span = match.span()
print(span)'''

''''txt = 'I love God'
match = re.search('God', txt, re.I)
print(match)

span = match.span()

start, end = span
print(start, end)
print(txt[start:end])'''


'''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
'''
#re.I - case ignore
matches = re.findall('[Pp]ython', txt)
print(matches)

matches = re.findall('python|Python', txt)

matches = re.findall('python', txt, re.I)


#replacing a substring
match_replaced = re.sub('[Pp]ython', 'Java', txt, re.I)
print(match_replaced)

match_replaced = re.sub('python|Python', 'Java', txt, re.I)
print(match_replaced)'''


''''txt = %I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?

replaced_matches = re.sub('%', '', txt)
print(replaced_matches)
print('YES!!!!!!!!')'''

#splitting text using regex split
''''txt = I am a teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?
print(re.split(, txt))
'''

#regex_pattern = r'apple'
#txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
''''match = re.findall(regex_pattern, txt)
print(match)

matches = re.findall(regex_pattern, txt, re.I)
print(matches)'''

''''regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern, txt)
print(matches)
'''
#OR

''''test = re.findall('[Aa]pple', txt)
print(test)'''


''''regex_pattern = r'\d' ocorrencias dos digitos de 0-9
txt = 'This regular expression example was made on December 6, 2019 on February 18, 2026'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'\d+'
txt = 'This regular expression example was made on December 6, 2019 on February 18, 2026'
matches = re.findall(regex_pattern, txt)
print(matches)'''

''''regex_pattern = r'[a].'

regex_pattern = r'[a].+'
txt = Apple and banana are fruits.
matches = re.findall(regex_pattern, txt)
print(matches)
'''

''''regex_pattern = r'[a].*' # a e qualquer char depois de a que apareca uma ou mais vezes
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print(matches)'''

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'
matches = re.findall(regex_pattern, txt)
print(matches)


txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches)