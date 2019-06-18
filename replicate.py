from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

the_connection_string = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;"
table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string = the_connection_string)

the_connection_string2 = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem2;AccountKey=Uvd627TNFSUqdUiXc6zAj6bIlEU1PAcgS6duKzB6RlPzKoINOlUHQHloAujsn15CvY1OJAxbyAvXBF3WTJHUwQ==;TableEndpoint=https://bigdatasystem2.table.cosmos.azure.com:443/;"
table_service2 = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string= the_connection_string2)