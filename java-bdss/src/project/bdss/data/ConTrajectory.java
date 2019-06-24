package project.bdss.data;

import com.microsoft.azure.storage.table.TableServiceEntity;

public class ConTrajectory extends TableServiceEntity {

	String edge;
	String near;
	String far;
	
	public ConTrajectory() {
		
	}
}
