from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

the_connection_string = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;"
table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string = the_connection_string)

userid = []
date = []
hour = []
minute = []
second = []
longitude = []
latitude = []
i = 0

for x in range(1,2): #10358 ~ data dari 1-10357
	with open("dataset/taxi_log_2008_by_id/{}.txt".format(str(x))) as f:
		for line in f:
			data = line.split(",")
			#userid.append(data[0])
			userid = data[0]

			datetime = data[1]
			partitionkey = datetime.replace("-","").replace(" ","").replace(":","")

			split = datetime.split(" ")
			#date.append(split[0])
			date = split[0]

			times = split[1].split(":")
			#hour.append(times[0])
			hour = times[0]
			#minute.append(times[1])
			minute = times[1]
			#second.append(times[2])
			second = times[2]

			#longitude.append(data[2])
			longitude = data[2]
			#latitude.append(data[3])
			latitude = data[3]

			entity = Entity()
			entity.PartitionKey = partitionkey
			entity.RowKey = edge_id
			entity.s_long = s_long
			entity.s_lat = s_lat
			entity.e_long = e_long
			entity.e_lat = e_lat
			entity.taxi_id = taxi_id
			entity.date = date
			entity.distance = distance
			table_service.insert_entity('dataset', entity)

			i += 1

