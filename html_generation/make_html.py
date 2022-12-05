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
    f.write('<style> body {background-color: black; color: white;} </style>\n')
    f.write('<style> a {text-decoration: none; color: rgb(150,150,150);} </style>\n')
    f.write('<style> object {border: 1px solid black; border-radius: 8px; max-width: 50vw;} </style>\n')
    f.write('</head>\n')

################################################################################
# FUNCTION: 
def write_title(f):
    f.write('<center><p>  </p><br>\n')
    f.write('<big><big>Light Upon Light</big></big><br>\n')
    f.write('by John Rugis<br><br>\n')
    f.write('A collection of forty small-screen photographs.<p>  </p><br>\n')
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
def write_photo(f, info):
    photos = info.split('$')
    for p in photos:
         details= p.split('%')
         f.write('<br><figure><object data="' + details[0][0:5] + '"></object><figcaption><small><small>' + details[0][5:] + '</small></figcaption></figure>\n')
         f.write('<p class="desc">' + details[1] + '</p></small><br>\n')
    

################################################################################
# FUNCTION: 
def write_photo_page(species, prev, next, info):
    gs = species.split('_')               # genus / species
    with open('../x' + species + '/' + SFNAME, 'w') as ofile:
        #
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body><span style="font-family: sans">\n')
        write_title(ofile)
        ofile.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="../index.html"><small>Contents</a></small><br>\n')
        #
        ofile.write('<p>  </p>\n')
        ofile.write('species: <big><i>' + gs[0] + ' ' + gs[1] + '</i></big><br>\n')
        ofile.write('<small>\n')
        ofile.write('&nbsp;&nbsp;&nbsp;<a href="../x' + prev + '/species.html">prev /</a>\n')
        ofile.write('<a href="../x' + next + '/species.html">next species</a>\n')
        ofile.write('</small><br>\n')
        #
        write_photos(ofile, info)
        #
        write_foot(ofile, '..')
        ofile.write('</span></body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def make_photo_pages(species, ifile):
    i = 0
    for line in ifile:
        iprev = len(species )-1 if (i == 0) else i-1                # previous species index
        inext = 0 if (i >= len(species )-1) else i+1  # next species index
        info = next(ifile).strip()
        write_species_page(species[i], species[iprev], species[inext], info)
        i += 1

################################################################################
# FUNCTION: 
def make_title_page(photos):
    with open('../' + IFNAME, 'w') as ofile:
        #
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body><span style="font-family: serif">\n')
        write_title(ofile)
        ofile.write('<center><a href="./x001/' + PFNAME + '">Click here to enter.</a></center><br>\n')
        ofile.write('</span>\n')
        ofile.write('<span style="font-family: helvetica">\n')
        write_foot(ofile)
        ofile.write('</span></body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def get_photo_list():
    slist = []
    with open(CFNAME) as ifile:
        for line in ifile:
            slist.append(line.strip())
    return(slist)

################################################################################
#
# MAIN PROGRAM: Create html files
#
################################################################################

photos = get_photo_list()
make_title_page(photos)
#with open(CFNAME) as ifile: make_photo_pages(photos, ifile)

################################################################################
################################################################################
