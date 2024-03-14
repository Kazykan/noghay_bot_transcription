import re

def determine_language(text: str):
    """Определить на каком языке писали."""
    try:
        a_string = re.sub(r'[^\w]+|[\d]+', r'',text[:20]).strip()
        if a_string[0] in 'ABDEFGHİIJKLMNOPRSŞTUVYZabdefghiıjklmnoprsştuvyzÄĞQÑÖÜäğqñöü':
            return "turkish"
        else:
            return "russian"
    except:
        return False