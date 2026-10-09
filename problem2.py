letter = '''dear <name>,
            you are selected for the position of <position> in our company.
              please report to the office on <date>.'''

print(letter.replace("<name>","devashish").replace("<position>","software engineer")
      .replace("<date>","1st Jan 2024"))