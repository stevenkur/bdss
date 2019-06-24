from xml.dom import minidom
import xml.etree.cElementTree as et
import pandas as pd
import csv
from itertools import zip_longest

def node_road():
	longdict= {}
	latdict= {}
	edge = 0
	xmldoc = et.parse('road_network.osm')
	df3cols = ['edge', 's_node', 'e_node', 's_lng', 's_lat', 'e_lng','e_lat']
	df3_xml = pd.DataFrame(columns=df3cols)
	for node in xmldoc.getroot():
		if(node.tag == 'node'): 
				point = node.attrib.get('id')
				longitude = node.attrib.get('lon')
				latitude = node.attrib.get('lat')
				longdict.update({point : longitude})
				latdict.update({point : latitude})
	for node in xmldoc.getroot():
		pointe = []
		if(node.tag == 'way'):
			tag = node.findall('tag')
			for t in tag:
				if (t.attrib.get('k') == 'highway'):
					vertex = node.findall('nd')
					for v in vertex:
						pointe.append(v.attrib.get('ref'))
					for i in range(1,len(pointe)):
						end = pointe[i]
						start = pointe[i-1]
						start_lat = latdict[start]
						start_long = longdict[start]
						end_lat = latdict[end]
						end_long = longdict[end]
					# length = len(pointe)
						df3_xml = df3_xml.append(
							pd.Series([edge,start,end,start_long,start_lat, end_long,end_lat],index=df3cols), 
							ignore_index=True
						)
						edge+=1
						print(edge)
	df3_xml.to_csv(r'edge_list.csv')
	print('finish')		
node_road()