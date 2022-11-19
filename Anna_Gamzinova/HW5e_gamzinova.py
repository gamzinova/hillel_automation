#  breaking the text into the sentences
import re

text = "The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that was launched into " \
       "low Earth orbit in 1990 and remains in operation.... It was not the first space telescope, but it is one of " \
       "the largest and most versatile, renowned both as a vital research tool and as a public relations boon for " \
       "astronomy. The Hubble telescope is named after astronomer Edwin Hubble and is one of NASA's Great " \
       "Observatories..... The Space Telescope Science Institute (STScI) selects Hubble's targets and processes the " \
       "resulting data, while the Goddard Space Flight Center (GSFC) controls the spacecraft.A commission headed by " \
       "Lew Allen, director of the Jet Propulsion Laboratory, was established to determine how the error could have " \
       "arisen. The Allen Commission found that a reflective null corrector, a testing device used to achieve a " \
       "properly shaped non-spherical mirror, had been incorrectly assembled—one lens was out of position by 1.3 mm (" \
       "0.051 in). "
# find all names without space separation ans replace dot with underscore
text_sub = re.sub(r'\.(\w*)\.', r'_\g<1>_', text)
# replace all two underscores with two dots
text_sub = re.sub(r'[_]{2}', r'..', text_sub)
# substitute the text by all non numeric '\.\s' to '.\n'
text_sub = re.sub(r'(\D)(\.+\s*)', r'\g<1>.\n', text_sub)
# substitute any underscore with a space
text_sub = re.sub(r'[_]', " ", text_sub)
# split text by '\n'
text_split = re.split('\n', text_sub)

# print(text_split)

for line in text_split:
    print(line)
