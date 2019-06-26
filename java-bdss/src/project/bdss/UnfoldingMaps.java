package project.bdss;

import processing.core.PApplet;
import de.fhpotsdam.unfolding.UnfoldingMap;
import de.fhpotsdam.unfolding.geo.Location;
import de.fhpotsdam.unfolding.marker.SimpleLinesMarker;
import de.fhpotsdam.unfolding.utils.MapUtils;
import de.fhpotsdam.unfolding.providers.Google;
import de.fhpotsdam.unfolding.providers.Microsoft;
import de.fhpotsdam.unfolding.providers.OpenStreetMap;
import de.fhpotsdam.unfolding.providers.OpenStreetMap.OpenStreetMapProvider;

@SuppressWarnings("serial")
public class UnfoldingMaps extends PApplet {
 
	private static final long serialVersionUID = 1L;
	UnfoldingMap map;
 
	
    public void setup() {
    	size(9500, 6000, P3D);
    	map = new UnfoldingMap(this, new Microsoft.RoadProvider());
		map.zoomAndPanTo(10, new Location(39.9180242, 116.4047904));
    }
 
    public void draw() {
    	background(230);
    	map.draw();
    }
 
}
