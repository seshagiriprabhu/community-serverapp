/* Define base layers */
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © openstreetmap contributors';
var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib}); 

var layer_geofences = new L.LayerGroup();
var array_geofences = new Array();
var markers = new L.markerClusterGroup();
var popup = L.popup();

/* Create custom marker which will represent 
locations in layer 'makers' */
customMarker = L.Marker.extend({
    options: { 
        title: 'User',
    }
});

var userEnteredIcon = L.icon({
    iconUrl: '/static/images/green-user-2x.png',
    iconRetinaUrl: '/static/images/green-user-2x.png',
    shadowUrl: '/static/images/marker-shadow.png',
    shadowRetinaUrl: '/static/images/marker-shadow.png',
    iconSize:     [40, 63],
    iconAnchor:   [20, 62],
    shadowAnchor: [4, 62],
    popupAnchor:  [-3, -76],
    shadowSize: [40, 63]
});

var userExitedIcon = new L.icon({
    iconUrl: '/static/images/red-user-2x.png',
    iconRetinaUrl: '/static/images/red-user-2x.png',
    shadowUrl: '/static/images/marker-shadow.png',
    shadowRetinaUrl: '/static/images/marker-shadow.png',
    iconSize:     [40, 63],
    iconAnchor:   [20, 62],
    shadowAnchor: [4, 62],
    popupAnchor:  [-3, -76],
    shadowSize: [40, 63]
});

/* Function to add geofences to 'array_geofences' */
function AddGeofenceToLayer() {
    for (var i=0; i<array_geofences.length; i++) {
        array_geofences[i].addTo(layer_geofences);
    }
}
/* Function which creates and adds new markers 
 based on filtered values */
function addMarkerLayers(val) {
    /* Fields in JSON that was returned */
    var fields = val.fields; 
    var t_type = "Exited";

    /* Parse point field to get values of latitude and longitude */
    var regExp = /\(([^)]+)\)/;
    var matches = regExp.exec(fields.geom);
    var point = matches[1];
    var lon=point.split(' ')[0];
    var lat=point.split(' ')[1];
    if (fields.t_type == 1) {
        t_type = "Entered";
        marker = new customMarker([lat, lon], {
            title: fields.disp_name,
            opacity: 1.0,
            icon: userEnteredIcon
        });
    } else {
        marker = new customMarker([lat, lon], {
            title: fields.disp_name,
            opacity: 1.0,
            icon: userExitedIcon
        });
    }

    var date_time = new Date(fields.date_time);
    var hour = date_time.getHours();
    var mins = date_time.getMinutes();
    var date = date_time.getDate();
    var month = date_time.getUTCMonth();
    var year = date_time.getYear();
    var final_format = hour + ":" + mins + " " 
             + date + "." + month + "." + year;
    marker.bindPopup("<strong>Name: </strong>" + fields.disp_name + 
            "<br><strong>Time: </strong>" + final_format + 
            "<br><strong>Transition Type: </strong>"+ t_type);
    markers.addLayer(marker);
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
/* Get all user location updates from DB */
$.ajax({
    url: '/data_analysis/location/',
    type: 'GET',
    contentType: "application/json",
    dataType: "json",
    success: function(response) {
        $.each(eval(response), function(key, val) {
            addMarkerLayers(val);
        });
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
    layers: [osm, markers, layer_geofences]
});

var baseLayers = {
    "OpenStreetMap": osm
};

var overlays = {
    "Geofences": layer_geofences,
    "User location updates": markers
};

/* Zoom to bounds in one easy click */
markers.on('clusterclick', function (a) {
    a.layer.zoomToBounds();
});

markers.on('click', function (a) {
    console.log('marker ' + a.layer);
});

markers.on('clusterclick', function (a) {
    console.log('cluster ' + a.layer.getAllChildMarkers().length);
});
/* A function to return the LatLng of a place clicked on mapped */
function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}
map.on('click', onMapClick);
L.control.layers(baseLayers, overlays).addTo(map);

/* S I D E B A R   F I L T E R */
L.easyButton('fa-bars', 
           function() {sidebar.toggle();},
        ''
    )
var sidebar = L.control.sidebar('sidebar', {
    position: 'left'
});
map.addControl(sidebar);

$('#filter_control').click(function() {
    sidebar.show();
});
/* Slider contrl */
$(document).ready(function() {  
    /* setting default min and max value for slider - period attribute */
    $("#slider_period").data("value", "365");
    $("#slider_period").slider({
        step: 10,
        min: 1,
        max: 365,
        slide: function( event, ui ) {
            $('#lbl').html(ui.value+" days");
            var selected_period = ui.value;
            $("#slider_period").data("value",selected_period);  
            getResult();
        }
    });
});
/* getResult function is called every time when user
filters map objects using sidebar filter */
function getResult() {
    /* Fetch value of all filter fields */
    var selected_user = $("#select_user").val();
    var selected_period = $("#slider_period").data("value");
    var selected_dayNight = $("#select_dayNight").val();

    /* Get fields where value is not 'all' so that you 
    later filter only those fields */
    var fields = new Array();
    
    if (selected_user != 'all') {
        fields.push("user");
    }
    if (selected_dayNight != 'all') {
        fields.push("daynight");
    }
    fields.push("period");
    /* Ajax call to get all apartments with defined filter values */
    $.ajax({
        url: '/data_analysis/location/filter/',
        type: 'GET',
        data: "user=" + selected_user + "&period=" + selected_period + 
        "&daynight=" + selected_dayNight + "&fields=" + fields,
        success: function(response) {
            /* First delete all markers from markers */
            markers.clearLayers();
            $.each(eval(response), function(key, val) {
                addMarkerLayers(val);
            });
        }
    });
}
