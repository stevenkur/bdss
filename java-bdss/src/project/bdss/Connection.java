package project.bdss;

import java.net.URISyntaxException;
import java.security.InvalidKeyException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

//Include the following imports to use table APIs
import com.microsoft.azure.storage.*;
import com.microsoft.azure.storage.table.*;
import com.microsoft.azure.storage.table.TableQuery.*;

import project.bdss.data.ConTrajectoryEntity;
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
	public List<String> QuerySTListTaxi(String startTime, String duration, String edge) {
	    List<String> taxi = new ArrayList<String>();
		try
		{
		    // Define constants for filters.
		    final String PARTITION_KEY = "PartitionKey";
		    final String ROW_KEY = "Edge_id";

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
		        System.out.println("STTrajectory_Taxi: " + entity.getPartitionKey() +
		            " " + entity.getRowKey() +
		            " " + entity.getEdge_id() +
		            " " + entity.getS_long() +
		            " " + entity.getS_lat() +
		            " " + entity.getE_long() +
		            " " + entity.getE_lat() +
		            " " + entity.getDistance() +
		            " " + entity.getTaxi_id() +
		            " " + entity.getTime_spent() +
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
	public String QuerySTTimeSpent(String taxi, String edge) {
	    String time = null;
	    Float count = Float.valueOf(0);
	    int i = 0;
		try
		{
		    // Define constants for filters.
		    final String PARTITION_KEY = "PartitionKey";
		    final String ROW_KEY = "Edge_id";
		    final String TAXI = "Taxi_id";

		    // Create a cloud table object for the table.
		    CloudTable cloudTable = tableClient.getTableReference("STTrajectory"); // table name

		    

		    String rowFilter = TableQuery.generateFilterCondition(
		        ROW_KEY,
		        QueryComparisons.EQUAL,
		        edge);

		    String taxiFilter = TableQuery.generateFilterCondition(
		        TAXI,
		        QueryComparisons.EQUAL,
		        taxi);

		    // Combine the two conditions into a filter expression.
		    String combinedFilter = TableQuery.combineFilters(taxiFilter,
		        Operators.AND, rowFilter);
		    

		    // Specify a range query
		    TableQuery<STTrajectoryEntity> rangeQuery =
		        TableQuery.from(STTrajectoryEntity.class)
		        .where(combinedFilter);

		    // Loop through the results, displaying information about the entity
		    for (STTrajectoryEntity entity : cloudTable.execute(rangeQuery)) {
		        System.out.println("STTrajectory_TimeSpent: " + entity.getTime_spent());
		    	count += Float.valueOf(entity.getTime_spent());
		    	i++;
		    }
		    count /= i;
		    time = String.valueOf(count);
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
		return time;
	}
	
	@SuppressWarnings("null")
	public List<String> QueryCon(String taxi_id, String edge) {
		Set<String> set = new HashSet<String>();
		try
		{
		    // Define constants for filters.
		    final String PARTITION_KEY = "PartitionKey";
		    final String ROW_KEY = "Edge_id";

		    // Create a cloud table object for the table.
		    CloudTable cloudTable = tableClient.getTableReference("ConTrajectory"); // table name

		    // Create a filter condition where the partition key is "Smith".
		    String partitionFilter = TableQuery.generateFilterCondition(
		        PARTITION_KEY,
		        QueryComparisons.EQUAL,
		        taxi_id);
		    
		    String rowFilter = TableQuery.generateFilterCondition(
			    ROW_KEY,
			    QueryComparisons.EQUAL,
			    edge);

			// Combine the two conditions into a filter expression.
			String combinedFilter = TableQuery.combineFilters(partitionFilter,
			        Operators.AND, rowFilter);

		    // Specify a range query, using "Smith" as the partition key,
		    // with the row key being up to the letter "E".
		    TableQuery<ConTrajectoryEntity> rangeQuery  =
		        TableQuery.from(ConTrajectoryEntity.class)
		        .where(combinedFilter);

		    // Loop through the results, displaying information about the entity
		    for (ConTrajectoryEntity entity : cloudTable.execute(rangeQuery)) {
		    	System.out.println("ConTrajectory: " + entity.getNext_edge());
		    	set.add(entity.getNext_edge());
		    }
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
		List<String> branch = new ArrayList<String>(set);
    	System.out.println("Branch: " + String.valueOf(branch));
		return branch;
	}
	
	@SuppressWarnings("null")
	public List<STTrajectoryEntity> QueryLatLong(String edge) {
		List<STTrajectoryEntity> data = new ArrayList<STTrajectoryEntity>();
		try
		{
		    // Define constants for filters.
		    final String ROW_KEY = "Edge_id";

		    // Create a cloud table object for the table.
		    CloudTable cloudTable = tableClient.getTableReference("STTrajectory"); // table name

		    String rowFilter = TableQuery.generateFilterCondition(
		        ROW_KEY,
		        QueryComparisons.EQUAL,
		        edge);

		    // Specify a range query
		    TableQuery<STTrajectoryEntity> rangeQuery =
		        TableQuery.from(STTrajectoryEntity.class)
		        .where(rowFilter);

		    // Loop through the results, displaying information about the entity
		    for (STTrajectoryEntity entity : cloudTable.execute(rangeQuery)) {
		        data.add(entity);
		    }
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
		return data;
	}
	
	public void Check() {
		
	}
}
