# re is a package for regular expression
#
# import re
#
# x="[abc]"
# matches=re.finditer(x,"abd xz4c")
# for match in matches:
#     print(match.start(),end=" ")
#     print(match.group())
#
#
# import re
# x="[^abcd]"
# matcher=re.finditer(x,"acfdhbzfwr413ac")
# for i in matcher:
#     print(i.start(),end=" ")
#     print(i.group())

# import re
# x="[a-z]"
# match=re.finditer(x,"vxsgcd5@#SDd")
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())

# import re
# x="[A-Z]"
# match=re.finditer(x,"yughdAESDRgf%$")
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())


# import re
# x="[a-zA-Z]"
# match=re.finditer(x,"yughdAESDRgf%$")
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())

# import re
# x="[0-9]"
# match=re.finditer(x,"gfh236rg5")
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())

# import re
# x="[^a-zA-Z0-9]"
# match=re.finditer(x,"%^gfSD65&gg$#gf#54")
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())






# import re
#
# x = "[\s]"
# match = re.finditer(x, "u uygd yuwged gygad gs ")
# for i in match:
#     print(i.start(), end=" ")
#     print(i.group())





# import re
# x = "[\d]"  # check the digits
#
# match = re.finditer(x, "uydt562yefd562ewre")
# for i in match:
#     print(i.start(), end=" ")
#     print(i.group())





#
# import re
#
# x = "[\D]"  #except all digits
# match = re.finditer(x, "yuewfg6523ge56g5")
# for i in match:
#     print(i.start(), end=" ")
#     print(i.group())




# import re
#
# x = "[\w]"  #all words except special characters
# match = re.finditer(x, "yuewfg6523ge56g5")
# for i in match:
#     print(i.start(), end=" ")
#     print(i.group())



# import re
#
# x = "[\W]"  #for all special characters
# match = re.finditer(x, "yu#ew*&fg()6{e5g5")
# for i in match:
#     print(i.start(), end=" ")
#     print(i.group())

import re
x="[a-zA-Z0-9]"
string="abcAbc123"
match=re.finditer(x,string)
for i in match:
  print(i.start(),end=" ")
  print(i.group())




