import re

text1 = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"

delete_numbers_from_text = re.sub("[0-9]+", "", text1)
print(delete_numbers_from_text)

text2 = "<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"

delete_html_from_text = re.sub(r"<.*?>", "", text2)
print(delete_html_from_text)

text3 = "Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. Mauris egestas erat " \
               "quam, ut faucibus eros congue et. In blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at " \
               "tristique augue risus eu risus."

delete_punctuation_from_text = re.sub("[.;,?!:]+", "", text3)
print(delete_punctuation_from_text)
