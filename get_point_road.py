from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from xml.dom import minidom

the_connection_string = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;"
table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string = the_connection_string)

xmldoc = minidom.parse('road_network')
point = xmldoc.getElementsByTagName('node')
road = xmldoc.getElementsByTagName('way')

i = 0
for s in point:
    point_id = s.attributes['id'].value
    latitude = s.attributes['lat'].value
    longitude = s.attributes['lon'].value

    entity = Entity()
    entity.PartitionKey = 'point'
    entity.RowKey = str(i)
    entity.point_id = point_id
    entity.latitude = latitude
    entity.longitude = longitude
    table_service.insert_entity('point', entity)

    i += 1

j = 0
for t in road:
	road_id = t.attributes['id'].value
	flag = 0
	points = []
	checktag = t.getElementsByTagName('tag')
	for e in checktag:
		if e.attributes['k'].value == 'highway':
			flag = 1
			pass
	if flag == 1:
		checknd = t.getElementsByTagName('nd')
		for v in checknd:
			points.append(v.attributes['ref'].value)
		start = points[0]
		end = points[len(checknd)-1]

		entity = Entity()
		entity.PartitionKey = 'road'
		entity.RowKey = str(j)
		entity.road_id = road_id
		entity.points = str(points)
		entity.start = start
		entity.end = end
		table_service.insert_entity('road', entity)

		j += 1