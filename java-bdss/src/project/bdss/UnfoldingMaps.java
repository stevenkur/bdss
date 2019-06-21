package project.bdss;

import de.fhpotsdam.unfolding.UnfoldingMap;
import de.fhpotsdam.unfolding.geo.Location;
import de.fhpotsdam.unfolding.providers.Microsoft;
import de.fhpotsdam.unfolding.utils.MapUtils;
import processing.core.PApplet;

public class UnfoldingMaps extends PApplet {
 
    UnfoldingMap map;
 
    public void setup() {
		size(800, 500);

		map = new UnfoldingMap(this, 0, 0, 900, 600, new Microsoft.RoadProvider());
		map.zoomAndPanTo(10, new Location(52.5f, 13.4f));
		MapUtils.createDefaultEventDispatcher(this, map);
    }
 
    public void draw() {
        background(000);
        size(800, 500);
        map.draw();
    }
 
}
