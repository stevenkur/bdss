package project.bdss;

import java.net.URISyntaxException;
import java.security.InvalidKeyException;
import java.util.ArrayList;
import java.util.List;

//Include the following imports to use table APIs
import com.microsoft.azure.storage.*;
import com.microsoft.azure.storage.table.*;
import com.microsoft.azure.storage.table.TableQuery.*;

import project.bdss.data.ConTrajectoryEntity;
import project.bdss.data.CustomerEntity;
import project.bdss.data.STTrajectoryEntity;

public class Connection {
	
	private String connectionString;
	private CloudStorageAccount storageAccount;
	private CloudTableClient tableClient;

	public void Initialize() throws InvalidKeyException, URISyntaxException {
		connectionString = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;";
	    storageAccount = CloudStorageAccount.parse(connectionString);
	    tableClient = storageAccount.createCloudTableClient();
	}

	public void ListTable() {
		try
		{
			int i = 0;
		    // Loop through the collection of table names.
		    for (String table : tableClient.listTables())
		    {
		        // Output each table name.
		        System.out.println("Table" + i + ": " + table);
		        i++;
		    }
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
	}
	
	@SuppressWarnings("null")
	public List<String> QueryST(String startTime, String duration, String edge) {
	    List<String> taxi = new ArrayList<String>();
		try
		{
		    // Define constants for filters.
		    final String PARTITION_KEY = "PartitionKey";
		    final String ROW_KEY = "RowKey";

		    // Create a cloud table object for the table.
		    CloudTable cloudTable = tableClient.getTableReference("STTrajectory"); // table name

		    String partitionFilter = TableQuery.generateFilterCondition(
		        PARTITION_KEY,
		        QueryComparisons.EQUAL,
		        startTime);

		    String rowFilter = TableQuery.generateFilterCondition(
		        ROW_KEY,
		        QueryComparisons.EQUAL,
		        edge);

		    // Combine the two conditions into a filter expression.
		    String combinedFilter = TableQuery.combineFilters(partitionFilter,
		        Operators.AND, rowFilter);

		    // Specify a range query
		    TableQuery<STTrajectoryEntity> rangeQuery =
		        TableQuery.from(STTrajectoryEntity.class)
		        .where(combinedFilter);

		    // Loop through the results, displaying information about the entity
		    for (STTrajectoryEntity entity : cloudTable.execute(rangeQuery)) {
		        System.out.println("STTrajectory: " + entity.getPartitionKey() +
		            " " + entity.getRowKey() +
		            " " + entity.getS_long() +
		            " " + entity.getS_lat() +
		            " " + entity.getE_long() +
		            " " + entity.getE_lat() +
		            " " + entity.getEdge_id() +
		            " " + entity.getDistance() +
		            " " + entity.getTaxi_id() +
		            " " + entity.getDate());
		    	taxi.add(entity.getTaxi_id());
		    }
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
		return taxi;
	}
	
	@SuppressWarnings("null")
	public List<String> QueryCon(String edge) {
	    List<String> branch = new ArrayList<String>();
		try
		{
		    // Define constants for filters.
		    final String PARTITION_KEY = "PartitionKey";

		    // Create a cloud table object for the table.
		    CloudTable cloudTable = tableClient.getTableReference("ConTrajectory"); // table name

		    // Create a filter condition where the partition key is "Smith".
		    String partitionFilter = TableQuery.generateFilterCondition(
		        PARTITION_KEY,
		        QueryComparisons.EQUAL,
		        edge);

		    // Specify a range query, using "Smith" as the partition key,
		    // with the row key being up to the letter "E".
		    TableQuery<ConTrajectoryEntity> partitionQuery  =
		        TableQuery.from(ConTrajectoryEntity.class)
		        .where(partitionFilter);

		    // Loop through the results, displaying information about the entity
		    for (ConTrajectoryEntity entity : cloudTable.execute(partitionQuery )) {
		    	System.out.println("ConTrajectory: " + entity.getRowKey());
		        branch.add(entity.getRowKey());
		    }
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
		return branch;
	}
	
	public void Check() {
		
	}
}
