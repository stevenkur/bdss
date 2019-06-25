package project.bdss.data;

import com.microsoft.azure.storage.table.TableServiceEntity;

public class STTrajectoryEntity extends TableServiceEntity {
	
	public STTrajectoryEntity(String hour, String edge_id) {
		this.partitionKey = hour;
		this.rowKey = edge_id;
	}
	
	public STTrajectoryEntity() { }

	String date;
	String distance;
	String s_long;
	String s_lat;
	String e_long;
	String e_lat;
	String taxi_id;
	String edge_id;

	public String getS_long() {
		return s_long;
	}

	public void setS_long(String s_long) {
		this.s_long = s_long;
	}

	public String getS_lat() {
		return s_lat;
	}

	public void setS_lat(String s_lat) {
		this.s_lat = s_lat;
	}

	public String getE_long() {
		return e_long;
	}

	public void setE_long(String e_long) {
		this.e_long = e_long;
	}

	public String getE_lat() {
		return e_lat;
	}

	public void setE_lat(String e_lat) {
		this.e_lat = e_lat;
	}

	public String getTaxi_id() {
		return taxi_id;
	}

	public void setTaxi_id(String taxi_id) {
		this.taxi_id = taxi_id;
	}

	public String getDate() {
		return date;
	}

	public void setDate(String date) {
		this.date = date;
	}

	public String getDistance() {
		return distance;
	}

	public void setDistance(String distance) {
		this.distance = distance;
	}

	public String getEdge_id() {
		return edge_id;
	}

	public void setEdge_id(String edge_id) {
		this.edge_id = edge_id;
	}
}
