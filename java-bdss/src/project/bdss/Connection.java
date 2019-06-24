package project.bdss;

import java.net.URISyntaxException;
import java.security.InvalidKeyException;

//Include the following imports to use table APIs
import com.microsoft.azure.storage.*;
import com.microsoft.azure.storage.table.*;
import com.microsoft.azure.storage.table.TableQuery.*;

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
}
