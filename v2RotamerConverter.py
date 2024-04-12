# this script converts the xyz coordinates from the OSPREY v2 rotamer library for an amenable format for Atomic_Ruler
# note: v2 coords must have newline at end

# change file and AA (3 letter abbrev) name
file1 = open('v2TrpCoords.csv', 'r')
rotamer_name = "Trp"

# setup
Lines = file1.readlines()
rotnum = 1
print("Rotamer " + str(rotnum))

# iterate over file by line
for line in Lines:
    # strip whitespace
    line1 = line.replace(' ', '')

    # empty lines = new rotamer
    if line1[0] == '\n':
        rotnum += 1
        print("Rotamer " + str(rotnum))

    # get xyz
    else:
        # iterate starting from "=" to "[" in v2 conflib (id # changes posn of xyz coords for some atoms, can't start from "[")
        count = 4
        while line1[count] != '[':
            count += 1
        reformx = []
        reformy = []
        reformz = []

        # get x
        count += 1
        while line1[count] != ',':
            reformx.append(line1[count])
            count += 1
        xnum = float("".join(reformx))

        # get y
        count += 1
        while line1[count] != ',':
            reformy.append(line1[count])
            count += 1
        ynum = float("".join(reformy))

        # get z
        count += 1
        while line1[count] != ']':
            reformz.append(line1[count])
            count += 1
        znum = float("".join(reformz))

        # get atom type
        count += 4
        atomtype = []
        while line1[count] != '\n':
            atomtype.append(line1[count])
            count += 1
        atype = str("".join(atomtype))

    # put items for a line in list format
    rotatom = [xnum, ynum, znum]

    # output formatted for OrderedDict
    print(rotamer_name + str(rotnum) + '[\'' + atype + '\']' + ' = ' + str(rotatom))

