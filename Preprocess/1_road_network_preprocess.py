from xml.dom import minidom
import xml.etree.cElementTree as et
import pandas as pd
import csv
from itertools import zip_longest


def osm_to_csv():
	longdict= {}
	latdict= {}
	edge = 0
	xmldoc = et.parse('road_network.osm') #load xml
	dfcols = ['node', 'lng', 'lat']
	df_xml = pd.DataFrame(columns=dfcols) #define dataframe
	df2cols = ['section_id','s_node','e_node','length']
	df2_xml = pd.DataFrame(columns=df2cols)
	df3cols = ['edge', 's_node', 'e_node', 's_lng', 's_lat', 'e_lng','e_lat']
	df3_xml = pd.DataFrame(columns=df3cols)
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
			longdict.update({point : longitude})
			latdict.update({point : latitude})
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
	df3_xml.to_csv(r'Edge.csv')
	print('finish')

def main():
	osm_to_csv()
	
if __name__ == "__main__":
	main()