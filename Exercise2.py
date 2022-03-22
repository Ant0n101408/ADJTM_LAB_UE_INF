import re

text1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista " \
           "egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta lobortis, " \
           "tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus."

find_hashtags_from_text= re.findall(r"#[a-z0-9_]+", text1)
print(find_hashtags_from_text)
