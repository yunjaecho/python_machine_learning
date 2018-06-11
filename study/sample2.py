title = "Seventeen year's of industry experience : Interested in machine learing I'm professional developer"
colon_position = title.index(':')
discard_text, post_colon_text = title[:colon_position], title[colon_position+1:]
print(discard_text)
print(post_colon_text)
pre_colon_text, _, post_colon_text = title.partition(':')
print(pre_colon_text)
print(post_colon_text)
post_colon_text = post_colon_text.replace('', '_')
print(post_colon_text)

from string import whitespace, punctuation

for character in whitespace + punctuation:
    post_colon_text = post_colon_text.replace(character, '_')

print(post_colon_text)

print(post_colon_text.upper())

print(post_colon_text.strip('_'))