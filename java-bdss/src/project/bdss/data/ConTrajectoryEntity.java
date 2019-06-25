package project.bdss.data;

import com.microsoft.azure.storage.table.TableServiceEntity;

public class ConTrajectoryEntity extends TableServiceEntity {

	public ConTrajectoryEntity(String taxi_id, String date_edge_id) {
		this.partitionKey = taxi_id;
		this.rowKey = date_edge_id;
	}
	
	public ConTrajectoryEntity() { }

	String edge_id;
	String previous;
	String next;
	
	public String getEdge_id() {
		return edge_id;
	}

	public void setEdge_id(String edge_id) {
		this.edge_id = edge_id;
	}

	public String getPrevious() {
		return previous;
	}

	public void setPrevious(String previous) {
		this.previous = previous;
	}

	public String getNext() {
		return next;
	}

	public void setNext(String next) {
		this.next = next;
	}
}
