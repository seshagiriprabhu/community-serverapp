/* Define base layers */
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © openstreetmap contributors';
var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib}); 

var layer_geofences = new L.LayerGroup();
var array_geofences = new Array();
var popup = L.popup();

/* Function to add geofences to 'array_geofences' */
function AddGeofenceToLayer() {
    for (var i=0; i<array_geofences.length; i++) {
        array_geofences[i].addTo(layer_geofences);
    }
}
/* Function to add filter through the json fields to add
geofences to map */
function addGeofencesToMap(val) {
    /* Fields in JSON that was returned */
    var fields = val.fields; 
    var lat = fields.latitude;
    var lon = fields.longitude;
    var rad = fields.geofence_radius;
    /* Function which creates and adds new circles 
    based on filtered values */
    var circle = L.circle(new L.LatLng(lat, lon), rad, {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.2,
        weight: 1,
        opacity: 0.3
    }); 
    circle.bindPopup("<strong>Geofence: </strong>" + fields.fence_name + 
        "<br><strong>Created by: </strong>" + fields.email); 
    circle.addTo(map);
    array_geofences.push(circle);
}
/* Get all geofences from DB */
$.ajax({
    url: '/data_analysis/geofence/',
    type: 'GET',
    contentType: "application/json",
    dataType: "json",
    success: function(response) {
        $.each(eval(response), function(key, val) {
            addGeofencesToMap(val);
        });
        // add geofence to layer and add it to map
        AddGeofenceToLayer();
    }
});
/* create map object */
var map = L.map('map', {
    center: [51.54521, 9.93267],
    zoom: 14,
    fullscreenControl: true,
    fullscreenControlOptions: {
        position: 'topleft'
    },
    layers: [osm, layer_geofences]
});

var baseLayers = {
    "OpenStreetMap": osm
};

var overlays = {
    "Geofences": layer_geofences,
};
L.control.layers(baseLayers, overlays).addTo(map);
