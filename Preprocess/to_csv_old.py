from xml.dom import minidom
import xml.etree.cElementTree as et
import pandas as pd
import csv
from itertools import zip_longest


	# point = xmldoc.getElementsByTagName('node')
	# road = xmldoc.getElementsByTagName('way')
def getvalueofnode(node):
	return node.text if node is not None else None

def node_to_csv():
	xmldoc = et.parse('road_network.osm') #load xml
	dfcols = ['node', 'lng', 'lat']
	df_xml = pd.DataFrame(columns=dfcols) #define dataframe
	
	for node in xmldoc.getroot():
		#get node tagged point in xml
		if(node.tag == 'node'): 
			point = node.attrib.get('id')
			longitude = node.attrib.get('lon')
			latitude = node.attrib.get('lat')
			df_xml = df_xml.append(
				pd.Series([point,longitude,latitude],index=dfcols), 
				ignore_index=True
				)
	df_xml.set_index('node')
	df_xml.to_csv(r'Point.csv')

def road_to_csv():
	xmldoc = et.parse('road_network.osm')
	df2cols = ['section_id','s_node','e_node','length']
	df2_xml = pd.DataFrame(columns=df2cols)
	for node in xmldoc.getroot():
		pointe=[]
		flag = 0
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
	df2_xml.set_index('section_id')
	df2_xml.to_csv(r'Network.csv')
road_to_csv()
node_to_csv()
	# for t in road:
	# 	road_ids = t.attributes['id'].value
	# 	flag = 0
	# 	points = []
	# 	checktag = t.getElementsByTagName('tag')
	# 	for e in checktag:
	# 		if e.attributes['k'].value == 'highway':
	# 			flag = 1
	# 			pass
	# 	if flag == 1:
	# 		checknd = t.getElementsByTagName('nd')
	# 		for v in checknd:
	# 			points.append(v.attributes['ref'].value)
	# 		start = points[0]
	# 		end = points[len(checknd)-1]
	# 		length = len(checknd)

	# 		section_id.append(road_ids)
	# 		s_node.append(start)
	# 		e_node.append(end)
	# 		length_road.append(length)

	# r = [section_id,s_node, e_node, length_road]
	# export_road_data = zip_longest(*r, fillvalue='')
	# with open('Road.csv', 'w', newline='') as out_file:
	#         writer = csv.writer(out_file)
	#         writer.writerow(('road_id','start','end','length'))
	#         writer.writerows(export_road_data)
	# out_file.close()
	# point_id = []
	# latitude = []
	# longitude = []
	# road_points = []
	# section_id = []
	# s_node = []
	# e_node = []
	# length_road = []
	# for t in road:
	# 	road_ids = t.attributes['id'].value
	# 	flag = 0
	# 	points = []
	# 	checktag = t.getElementsByTagName('tag')
	# 	for e in checktag:
	# 		if e.attributes['k'].value == 'highway':
	# 			flag = 1
	# 			pass
	# 	if flag == 1:
	# 		checknd = t.getElementsByTagName('nd')
	# 		for v in checknd:
	# 			points.append(v.attributes['ref'].value)
	# 		start = points[0]
	# 		end = points[len(checknd)-1]
	# 		length = len(checknd)
	# 		section_id.append(road_ids)
	# 		s_node.append(start)
	# 		e_node.append(end)
	# 		length_road.append(length)
	# r = [section_id,s_node, e_node, length_road]
	# export_road_data = zip_longest(*r, fillvalue='')
	# with open('Road.csv', 'w', newline='') as out_file:
	#         writer = csv.writer(out_file)
	#         writer.writerow(('road_id','start','end','length'))
	#         writer.writerows(export_road_data)
	# out_file.close()
	# for s in point:
	#     point_id.append(s.attributes['id'].value)
	#     latitude.append(s.attributes['lat'].value)
	#     longitude.append(s.attributes['lon'].value)
	# d = [point_id,latitude,longitude]
	# export_data = zip_longest(*d, fillvalue='')
	# with open('PointNode.csv', 'w', newline='') as out_file:
	#         writer = csv.writer(out_file)
	#         writer.writerow(('point_id','lat','lon'))
	#         writer.writerows(export_data)
	# out_file.close()
