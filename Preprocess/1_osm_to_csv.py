from xml.dom import minidom
import xml.etree.cElementTree as et
import pandas as pd
import csv
from itertools import zip_longest


	# point = xmldoc.getElementsByTagName('node')
	# road = xmldoc.getElementsByTagName('way')
def getvalueofnode(node):
	return node.text if node is not None else None

def osm_to_csv():
	xmldoc = et.parse('road_network.osm') #load xml
	dfcols = ['node', 'lng', 'lat']
	df_xml = pd.DataFrame(columns=dfcols) #define dataframe
	df2cols = ['section_id','s_node','e_node','length']
	df2_xml = pd.DataFrame(columns=df2cols)
	for node in xmldoc.getroot():
		pointe=[]
		flag = 0
		#get node tagged point in xml
		if(node.tag == 'node'): 
			point = node.attrib.get('id')
			longitude = node.attrib.get('lon')
			latitude = node.attrib.get('lat')
			df_xml = df_xml.append(
				pd.Series([point,longitude,latitude],index=dfcols), 
				ignore_index=True
				)
		if(node.tag == 'way'):
			tag = node.findall('tag')
			if(tag is not None):
				for t in tag:
					if (t.attrib.get('k') == 'highway'):
						road = node.attrib.get('id')
						vertex = node.findall('nd')
						for v in vertex:
							pointe.append(v.attrib.get('ref'))
						start = pointe[0]
						end = pointe[len(pointe)-1]
						length = len(pointe)
						df2_xml = df2_xml.append(
							pd.Series([road,start,end,length],index=df2cols), 
							ignore_index=True
						)
		print('ongoing')
	df_xml.to_csv(r'Point.csv')
	df2_xml.to_csv(r'Network.csv')
	print('finish')
osm_to_csv()
	