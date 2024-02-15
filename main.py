# Quick & dirty usage instructions:
#
# Make a copy of the Traktor collection.nml file that contains the playlist you want to shuffle
# Change the copy's file extension from .nml to .xml - that's now your input file
#
# Load this file (main.py) and your input file in https://www.online-python.com/
# Set inputFile = your input filename
# Set playlistName = your playlist name
# Click 'Run', then download the output file
# Delete the last four lines of the output file
# Then paste it into your collection.nml

import random
import xml.etree.ElementTree as ET


inputFile = 'collection.xml'  # set to your input filename
playlistName = 'my playlist'  # set to your playlist name


tree = ET.parse(inputFile)
root = tree.getroot()

playlistToShuffle = None

for NODE in root.iter('NODE'):
    if 'TYPE' and 'NAME' in NODE.attrib and NODE.attrib['TYPE'] == 'PLAYLIST' and NODE.attrib['NAME'] == playlistName:
        playlistNode = NODE


playlists = []
playlistToShuffle = None
for child in playlistNode:
    if child.tag == 'PLAYLIST':
        playlists.append(child)
if playlists:
    playlistToShuffle = playlists[0]

entries = playlistToShuffle.findall('ENTRY')

# Remove the entries from playlistToShuffle (they will be added later
# in a different order).
for entry in entries:
    playlistToShuffle.remove(entry)

# Shuffle the order of the entries
random.shuffle(entries)

# add the entries back to playlistToShuffle
for entry in entries:
    playlistToShuffle.append(entry)


for subelement in playlistToShuffle.iter():
    if subelement.tag == 'PRIMARYKEY':
        for item in subelement.iter():
            itemKey = item.attrib['KEY']
            itemKeyAmpersandsReplaced = itemKey.replace('&', '&amp;')
            print(f'<ENTRY><PRIMARYKEY TYPE="TRACK" KEY="{itemKeyAmpersandsReplaced}"></PRIMARYKEY>\n</ENTRY>')
