package project.bdss;

import processing.core.PApplet;
import de.fhpotsdam.unfolding.UnfoldingMap;
import de.fhpotsdam.unfolding.geo.Location;
import de.fhpotsdam.unfolding.utils.MapUtils;
import de.fhpotsdam.unfolding.providers.Google;

@SuppressWarnings("serial")
public class UnfoldingMaps extends PApplet {
 
	UnfoldingMap map;

	public void setup() {
		size(800, 600, OPENGL);

		map = new UnfoldingMap(this, new Google.GoogleMapProvider());
		map.zoomAndPanTo(20, new Location(39.9310978, 116.3197656));

		MapUtils.createDefaultEventDispatcher(this, map);
	}

	@SuppressWarnings("deprecation")
	public void draw() {
		background(0);
        resize(800, 600);
		map.draw();
	}
 
}
