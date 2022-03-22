import re

text5 = "Lorem :) ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista " \
      "egestas erat :| ;/ #tweetext ;) quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta lobortis, " \
      "tortor nisl facilisis :-D leo, :> at tristique #frasistas augue risus eu risus."

find_emoticons_from_text = re.findall(r"[:;][-]?[/|)(><D]", text5)
print(find_emoticons_from_text)
