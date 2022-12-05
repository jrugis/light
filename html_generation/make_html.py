################################################################################
# Create html files for web site:
# The Developmental Morphology of New Zealand Native Ferns 
# 18.11.22 J. Rugis
#
################################################################################

# user settings
CFNAME = 'contents.txt'
IFNAME = 'index.html'
PFNAME = 'photo.html'

# global variables

################################################################################
# FUNCTION: 
def write_head(f):
    f.write('<head>\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<style> body {background-color: rgb(50,50,50); color: white;} </style>\n')
    f.write('<style> a {text-decoration: none; color: rgb(150,150,150);} </style>\n')
    f.write('<style> img {border: 1px solid black; width: 100%; height: auto;} </style>\n')
    #f.write('<style> img {border: 1px solid black; width: 100%; max-height: 100%;} </style>\n')
    f.write('</head>\n')

################################################################################
# FUNCTION: 
def write_title(f):
    f.write('<center><p>  </p><br>\n')
    f.write('<big><big>Light Upon Light</big></big><br>\n')
    f.write('by John Rugis<br><br>\n')
    f.write('A collection of forty photographs for a small-screen.<p>  </p><br>\n')
    f.write('</center>\n')

################################################################################
# FUNCTION: 
def write_foot(f):
    f.write('<center><p>  </p><br>\n')
    f.write('<small><small><small>\n')
    f.write('(c)2022 J.Rugis, \n')
    f.write('jrugis@gmail.com\n')
    f.write('</small></small></small><p>  </p>\n')
    f.write('<img src="./by-sa.svg"></center>\n')

################################################################################
# FUNCTION: 
def write_photo(f, curr, info):
    details = info.split('#')
    f.write('<br><figure><img src="./photos/' + details[0] + '"><figcaption><small><small>#' + curr + ' ' + details[1] + '</small></figcaption></figure>\n')

################################################################################
# FUNCTION: 
def write_photo_page(curr, prev, next, info):
    with open('../x' + curr + PFNAME, 'w') as ofile:
        #
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body><span style="font-family: sans">\n')
        #
        write_photo(ofile, curr, info)
        ofile.write('<center>\n')
        ofile.write('<a href="./x' + prev + PFNAME + '">prev &nbsp;&nbsp;&nbsp;</a>\n')
        ofile.write('<a href="./x' + next + PFNAME + '">next &nbsp;&nbsp;&nbsp;</a>\n')
        ofile.write('<a href="./' + IFNAME + '">home</a>\n')
        ofile.write('</center>\n')
        ofile.write('</span></body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def make_photo_pages(ifile):
    i = 0
    for line in ifile:
        iprev = 0 if (i == 0) else i-1  # previous species index
        inext = 40 if (i >= 40) else i+1  # next species index
        write_photo_page(str(i+1), str(iprev+1), str(inext+1), line.strip())
        i += 1

################################################################################
# FUNCTION: 
def make_title_page():
    with open('../' + IFNAME, 'w') as ofile:
        #
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body><span style="font-family: serif">\n')
        write_title(ofile)
        ofile.write('<center><a href="./x1' + PFNAME + '">Click here to enter.</a></center><br>\n')
        ofile.write('</span>\n')
        ofile.write('<span style="font-family: helvetica">\n')
        write_foot(ofile)
        ofile.write('</span></body>\n')
        ofile.write('</html>\n')

################################################################################
#
# MAIN PROGRAM: Create html files
#
################################################################################

make_title_page()
with open(CFNAME) as ifile: make_photo_pages(ifile)

################################################################################
################################################################################
