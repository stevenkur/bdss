package project.bdss;

import java.net.URISyntaxException;
import java.security.InvalidKeyException;

//Include the following imports to use table APIs
import com.microsoft.azure.storage.*;
import com.microsoft.azure.storage.table.*;
import com.microsoft.azure.storage.table.TableQuery.*;

import project.bdss.data.STTrajectory;

public class Connection {
	
	private String connectionString;
	private CloudStorageAccount storageAccount;
	private CloudTableClient cloudTableClient;

	public void Initialize() throws InvalidKeyException, URISyntaxException {
		connectionString = "DefaultEndpointsProtocol=https;AccountName=bigdatasystem;AccountKey=dlGS2h7vRiEdwRjGw1R2UqCr3QcJUGzfQjeyULj12Ssf1NtKwA11upx3uu1x1KLTBUzX00waXTelLQfY6oQ9BA==;TableEndpoint=https://bigdatasystem.table.cosmos.azure.com:443/;";
	    storageAccount = CloudStorageAccount.parse(connectionString);
	    cloudTableClient = storageAccount.createCloudTableClient();
	}

	public void ListTable() {
		try
		{
		    // Retrieve storage account from connection-string.
		    CloudStorageAccount storageAccount =
		        CloudStorageAccount.parse(connectionString);

		    // Create the table client.
		    CloudTableClient tableClient = storageAccount.createCloudTableClient();

		    // Loop through the collection of table names.
		    for (String table : tableClient.listTables())
		    {
		        // Output each table name.
		        System.out.println(table);
		    }
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
	}
	
	public void QueryST() {
		try
		{
		    // Define constants for filters.
		    final String PARTITION_KEY = "PartitionKey";
		    final String ROW_KEY = "RowKey";
		    final String TIMESTAMP = "Timestamp";

		    // Create the table client.
		    CloudTableClient tableClient = storageAccount.createCloudTableClient();

		    // Create a cloud table object for the table.
		    CloudTable cloudTable = tableClient.getTableReference("STTrajectory"); // table name

		    // Create a filter condition where the partition key is "Smith".
		    String partitionFilter = TableQuery.generateFilterCondition(
		        PARTITION_KEY,
		        QueryComparisons.EQUAL,
		        "Smith");

		    // Create a filter condition where the row key is less than the letter "E".
		    String rowFilter = TableQuery.generateFilterCondition(
		        ROW_KEY,
		        QueryComparisons.LESS_THAN,
		        "E");

		    // Combine the two conditions into a filter expression.
		    String combinedFilter = TableQuery.combineFilters(partitionFilter,
		        Operators.AND, rowFilter);

		    // Specify a range query, using "Smith" as the partition key,
		    // with the row key being up to the letter "E".
		    TableQuery<STTrajectory> rangeQuery =
		        TableQuery.from(STTrajectory.class)
		        .where(combinedFilter);

		    // Loop through the results, displaying information about the entity
//		    for (STTrajectory entity : cloudTable.execute(rangeQuery)) {
//		        System.out.println(entity.getPartitionKey() +
//		            " " + entity.getRowKey() +
//		            "\t" + entity.getEmail() +
//		            "\t" + entity.getPhoneNumber());
//		    }
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
	}
	
	public void QueryCon() {
		try
		{
		    // Define constants for filters.
		    final String PARTITION_KEY = "PartitionKey";
		    final String ROW_KEY = "RowKey";
		    final String TIMESTAMP = "Timestamp";

		    // Create the table client.
		    CloudTableClient tableClient = storageAccount.createCloudTableClient();

		    // Create a cloud table object for the table.
		    CloudTable cloudTable = tableClient.getTableReference("ConTrajectory"); // table name

		    // Create a filter condition where the partition key is "Smith".
		    String partitionFilter = TableQuery.generateFilterCondition(
		        PARTITION_KEY,
		        QueryComparisons.EQUAL,
		        "Smith");

		    // Create a filter condition where the row key is less than the letter "E".
		    String rowFilter = TableQuery.generateFilterCondition(
		        ROW_KEY,
		        QueryComparisons.LESS_THAN,
		        "E");

		    // Combine the two conditions into a filter expression.
		    String combinedFilter = TableQuery.combineFilters(partitionFilter,
		        Operators.AND, rowFilter);

		    // Specify a range query, using "Smith" as the partition key,
		    // with the row key being up to the letter "E".
		    TableQuery<STTrajectory> rangeQuery =
		        TableQuery.from(STTrajectory.class)
		        .where(combinedFilter);

		    // Loop through the results, displaying information about the entity
//		    for (STTrajectory entity : cloudTable.execute(rangeQuery)) {
//		        System.out.println(entity.getPartitionKey() +
//		            " " + entity.getRowKey() +
//		            "\t" + entity.getEmail() +
//		            "\t" + entity.getPhoneNumber());
//		    }
		}
		catch (Exception e)
		{
		    // Output the stack trace.
		    e.printStackTrace();
		}
	}
}
