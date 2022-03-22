import re


def clean_text(txt: str) -> str:
    find_emoticons_from_text = re.findall(r"[:;][-]?[/\|\)\(><D]", txt)
    txt_low_from_text = txt.lower()
    delete_numbers_from_text = re.sub("[0-9]+", "", txt_low_from_text)
    delete_html_from_text = re.sub(r'<.*?>', '', delete_numbers_from_text)
    delete_punctuation_from_text = re.sub(r"[^\w\s]", " ", delete_html_from_text)
    delete_whitespace_from_text = delete_punctuation_from_text.strip()
    clean_txt = delete_whitespace_from_text + ' '.join(find_emoticons_from_text)
    return clean_txt
