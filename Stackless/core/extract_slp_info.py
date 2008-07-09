################################################################
#
# extract_slp_info.py
#
# extract slotnames from typeonject.c and create a structure
# for inclusion into PyHeaptypeObject.
#
################################################################

srcname = "../../Objects/typeobject.c"
dstname = "slp_exttype.h"

def parse():
    f = open(srcname)
    line = ""
    slots = []
    buf = ""
    for line in f:
        if line.endswith("\\\n"):
            buf += line
        else:
            feed(buf+line, slots)
            buf = ""
    return slots

def feed(line, slots):
    pieces = line.split("(")
    if len(pieces) < 2:
        return
    first = pieces[0].strip()
    if len(first.split()) > 1:
        return
    if first.startswith("COPY"):
        print(line)
        slot = pieces[1].split(")")[0].strip()
    elif first.endswith("SLOT"):
        print(line)
        slot = pieces[1].split(",")[1].strip()
    else:
        return
    if slot not in slots:
        slots.append(slot)

def generate():
    slotnames = parse()
    f = open(dstname, "w")
    print("""\
/*
 * this file was generated from typeobject.c using the script
 * Stackless/core/extract_slp_info.py .
 * please don't edit this output, but work on the script.
 */

typedef struct _slp_methodflags {\
""", file=f)
    for slot in slotnames:
        print("\tsigned char %s;" % slot, file=f)
    print("} slp_methodflags;", file=f)

if __name__ == "__main__":
    generate()
