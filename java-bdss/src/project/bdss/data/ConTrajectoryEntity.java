package project.bdss.data;

import com.microsoft.azure.storage.table.TableServiceEntity;

public class ConTrajectoryEntity extends TableServiceEntity {

	public ConTrajectoryEntity(String taxi_id, String date_edge_id) {
		this.partitionKey = taxi_id;
		this.rowKey = date_edge_id;
	}
	
	public ConTrajectoryEntity() { }

	String edge_id;
	String previous_edge;
	String next_edge;
	
	public String getEdge_id() {
		return edge_id;
	}

	public void setEdge_id(String edge_id) {
		this.edge_id = edge_id;
	}

	public String getPrevious_edge() {
		return previous_edge;
	}

	public void setPrevious_edge(String previous_edge) {
		this.previous_edge = previous_edge;
	}

	public String getNext_edge() {
		return next_edge;
	}

	public void setNext_edge(String next_edge) {
		this.next_edge = next_edge;
	}
}
