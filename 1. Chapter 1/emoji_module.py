#pip install emoji
#pip install emoji --upgrade
#Use the emoji cheat sheet to find your favorite emoji
# https://www.webfx.com/tools/emoji-cheat-sheet/
# http://www.unicode.org/emoji/charts/full-emoji-list.html

from emoji import emojize
print(emojize(":thumbs_up: :sunglasses:"))
import emojis
emojified = emojis.encode("There is a :snake: in my boot !")
print(emojified)
