words = """{'Verb': ['call upon in supplication; entreat', 'make a solicitation or entreaty for something; request urgently or persistently', 'ask to obtain free', 'dodge, avoid answering, or take for granted']}"""
clean_words = words.strip("""{[]}""")
cleaner_words = clean_words.replace("[", "")
print(cleaner_words)