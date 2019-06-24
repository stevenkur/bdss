package project.bdss.data;

import com.microsoft.azure.storage.table.TableServiceEntity;

public class STTrajectory extends TableServiceEntity {

	String matchedEdgeLat;
	String matchedEdgeLong;
	String matchedNodeLat;
	String matchedNodeLong;
	
	public STTrajectory(String matchedEdgeLat, String matchedEdgeLong, String matchedNodeLat, String matchedNodeLong) {
		super();
		this.matchedEdgeLat = matchedEdgeLat;
		this.matchedEdgeLong = matchedEdgeLong;
		this.matchedNodeLat = matchedNodeLat;
		this.matchedNodeLong = matchedNodeLong;
	}
	
	public STTrajectory() {
		
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
