package project.bdss.data;

import com.microsoft.azure.storage.table.TableServiceEntity;

public class ConnectionTrajectory extends TableServiceEntity {

	String matchedEdgeLat;
	String matchedEdgeLong;
	String matchedNodeLat;
	String matchedNodeLong;
	
	public ConnectionTrajectory() {
		
	}

	public String getMatchedEdgeLat() {
		return matchedEdgeLat;
	}

	public void setMatchedEdgeLat(String matchedEdgeLat) {
		this.matchedEdgeLat = matchedEdgeLat;
	}

	public String getMatchedEdgeLong() {
		return matchedEdgeLong;
	}

	public void setMatchedEdgeLong(String matchedEdgeLong) {
		this.matchedEdgeLong = matchedEdgeLong;
	}

	public String getMatchedNodeLat() {
		return matchedNodeLat;
	}

	public void setMatchedNodeLat(String matchedNodeLat) {
		this.matchedNodeLat = matchedNodeLat;
	}

	public String getMatchedNodeLong() {
		return matchedNodeLong;
	}

	public void setMatchedNodeLong(String matchedNodeLong) {
		this.matchedNodeLong = matchedNodeLong;
	}
}
