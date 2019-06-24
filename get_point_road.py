from xml.dom import minidom


xmldoc = minidom.parse('road_network')
point = xmldoc.getElementsByTagName('node')
road = xmldoc.getElementsByTagName('way')

for s in point:
    point_id = s.attributes['id'].value
    latitude = s.attributes['lat'].value
    longitude = s.attributes['lon'].value
    with open('Point.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows((point_id, latitude, longitude))

# for t in road:
# 	road_id = t.attributes['id'].value
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

# 		entity = Entity()
# 		entity.PartitionKey = 'road'
# 		entity.RowKey = str(j)
# 		entity.road_id = road_id
# 		entity.points = str(points)
# 		entity.start = start
# 		entity.end = end
# 		table_service.insert_entity('road', entity)