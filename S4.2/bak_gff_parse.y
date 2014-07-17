## Module to help with GFF parsing
##
# Available functions:
# gff_to_list(fh)
# gff_to_dict(l_lines)
#

# Convert a gff file to a list
# Input: String corresponding to GFF file path
# Output: List where each line corresponds to a single
# Function opens and closes file
def gff_to_list(s_gff_file):
    fh_gff = open(s_tff_file , 'r')
    l_lines = fh_gff.readlines()
    fh_gff.close()
    return l_lines

# iterate over the gff line list and create a dictionary entry for each line
# Input: list of gff lines
# output Dictionary of gff lines
# Dictionary format:
# Key: LocusID
# Value: list
#        Value[0]: LocusID
#        Value[1]: accession
#        Value[2]: GI
#        Value[3]: scaffoldId
#        Value[4]: start
#        Value[5]: stop
#        Value[6]: strand
#        Value[7]: sysName
#        Value[8]: name
#        Value[9]: desc
#        Value[10]: COG
#        Value[11]: COGFun
#        Value[12]: COGDesc
#        Value[13]: TIGRFam
#        Value[14]: TIGRRoles
#        Value[15]: GO
#        Value[16]: EC
#        Value[17]: ECDesc
def gff_to_dict(l_lines):
    d_gff = {}
    for line in l_lines:
        l_splitline = line.split('\t')
        d_gff[l_splitline[0]]=l_splitline
    return d_gff
