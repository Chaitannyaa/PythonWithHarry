# import os

# oldname = "sample2.txt"
# newname = "renamed_by_python.txt"
# with open(oldname) as f:
#     content = f.read()

# with open(newname, "w") as f:
#     f.write(content)

# os.remove(oldname)

import os
with open("Pls_delete.txt", 'r') as f:
    content=f.read()
with open("Renamed by OS module.txt", 'w') as f:
    f.write(content)
remove="Pls_delete.txt"
os.remove(remove)
