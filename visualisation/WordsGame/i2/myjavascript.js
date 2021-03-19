
var count = 0;
var maxCount = 5000;
var maxChartData = 40;
var interval = 5000;
var processing = false;
var sName = "3-axis Accelerometer";
//alert(sName);
var sensorsList = [sName]//["3-axis Accelerometer":3];
var timePoint = 0;
var elapsed = 0;
var _Sec = 1;
var _USec = 0;
var ssName = "";
var oldName = "";
var cancel = false;
var chartDataCount=0;

// Blank Data
var data  = {};

//Option for graph
var locales = {
  en: {
    edit: 'Edit',
    del: 'Delete selected',
    back: 'Back',
    addNode: 'Add Node',
    addEdge: 'Add Edge',
    editNode: 'Edit Node',
    editEdge: 'Edit Edge',
    addDescription: 'Click in an empty space to place a new node.',
    edgeDescription: 'Click on a node and drag the edge to another node to connect them.',
    editEdgeDescription: 'Click on the control points and drag them to a node to connect to it.',
    createEdgeError: 'Cannot link edges to a cluster.',
    deleteClusterError: 'Clusters cannot be deleted.',
    editClusterError: 'Clusters cannot be edited.'
  }
}
var options = {
	autoResize: true,
	height: '100%',
	width: '100%',
	locale: 'en',
	locales: locales,
	clickToUse: false,
	physics:true,
    configure:function (option, path) {
      if (path.indexOf('smooth') !== -1 || option === 'smooth') {
        return true;
      }
      return false;
    },
    edges: {
      smooth: {
        type: 'continuous'
      }
    }
};
	

$(document).ready(function() {
	// This will get the first returned node in the jQuery collection.
	var container = document.getElementById("mynetwork");
	var nodes = new vis.DataSet([
	]);

  // create an array with edges
	var edges = new vis.DataSet([
	]);
	
	data = {
    nodes: nodes,
    edges: edges
	};
	// Network options


	var network = new vis.Network(container, data, options);
	process();
	
});

function process() {
	if (cancel) return;
	if (processing) {
		setTimeout(process, interval);
		return;
	}
	else {
		
		processing = true;
		ssName = "";
		oldName = "";
	
		$.ajax({
		   method: "POST",
		   url: "getMongoDB.php",
		   data: { lastSec : _Sec, lastUSec : _USec }
		})
		.done(function( json_data ) {
			if (count > 0) $("#count_data").text(count);
			var msg = jQuery.parseJSON(json_data);
			var content = "";
			var datatxt = "";
			var timetxt = "";
			var innerCount=0;
			$.each( msg, function( i, row ) {
				innerCount = innerCount + 1;
				timetxt = "<i>" + innerCount + "</i>. [Sec= " + row["timeSec"]  + ". USecs: " +  row["timeUSec"] + "] : ";
				if (_Sec < row["timeSec"]) {
				   _Sec = row["timeSec"];
				   _USec = row["timeUSec"];
				}
				else if (_Sec == row["timeSec"] && _USec < row["timeUSec"]) {
				   _USec = row["timeUSec"];
				} 	
				
				datatxt = "<b>" + row["nodes"] + "</b> || '"+ row["edges"] + "'";
				content += "<div>" + timetxt + datatxt + "</div> <br>";
				$("#return_data").html(content);
				
				// Now play with the data. Kakakak
				try {
					// Start with nodes
					var node_srt = row["nodes"].substring(2, row["nodes"].length-2);
					var node_list = node_srt.split("\", \"");	// Get list of new nodes
					var edge_srt = row["edges"].substring(2, row["edges"].length-2);
					var edge_list = edge_srt.split("\", \"");	// Get list of new edges
					var nd;
					var ed;
					
					
					// Delete edges are longer in graph
					var toeliItems=[];
					var current_edges = data.edges.get();
					for (ed in current_edges){
						//alert(current_edges[ed].id + "XxX" + !(edge_list.indexOf(current_edges[ed].id) >= 0) +"XxX"+ edge_list);
						// get to the left of ':' 
						idstr = current_edges[ed].id;
						idstr = idstr.substring(0, idstr.indexOf(":"));
						if (!(edge_list.indexOf(idstr) >= 0)){
							toeliItems.push(idstr);
						}
					}
					
					for (ed in toeliItems) {
						data.edges.remove(toeliItems[ed]);
					}
					
					
					// Delete nodes are longer in graph
					toeliItems=[];
					var current_nodes = data.nodes.get();
					for (nd in current_nodes){
						idstr = current_nodes[nd].id;
						idstr = idstr.substring(0, idstr.indexOf(":"));
						if (!(node_list.indexOf(idstr) >= 0)){
							toeliItems.push(idstr);
						}
					}
					//alert(toeliItems.length);
					for (nd in toeliItems) {
						data.nodes.remove(toeliItems[nd]);
					}
					
					// Add new nodes					
					for (nd in node_list) {
						res = nd.split(":");
						if (res.length == 2 data.nodes.get(res[0]) == null)
							data.nodes.add({id: res[0],  value: Number(res[1]), label: res[0]});
					}
				
					// Add new edges
					for (ed in edge_list) {
						res = edge_list[ed].split(" ");
						if (res.length == 2)
							// Split the second element to get freq
							res2 = res[1].split(":");
							if (res2.length == 2 && data.edges.get(res[0] + ' ' +res2[0]) == null)
							data.edges.add({id: (res[0] + ' ' +res2[0]), from: res[0], to: res2[0], value: Number(res2[1]),arrows:'to'});
					}					
				}
				catch(err) {
					alert(err.message);
				}
				
				
					
				
					
				//alert(content);
				/*
				 //Add data to chart
				if (ssName == sName) {
					if (chartDataCount > maxChartData) {
					//	alert("Hello! I am an alert box!!");
						myLineChart.removeData();
						chartDataCount--;
					}
					
					if (timePoint == 0) timePoint = _Sec;
					var xText = "";
					if (elapsed != _Sec - timePoint) {
						elapsed = _Sec - timePoint;
						xText = elapsed;
					}
					myLineChart.addData( row["values"], xText );
					chartDataCount++;
				}
				*/
				
				$("#network_stats").html("Num. of node:" + data.nodes.length + ". Num. of edge:" + data.edges.length);
			
			});
			
			if (count > 0) {
				
				// Update sensor data
			//$("#return_data").html(innerCount);
			//	data.nodes.add({id: count, label: count});
			}
			processing = false;
			count++;
		});
		
		if (count < maxCount) {
			setTimeout(process, interval);
		}
	}
}

function pause() {
	if (!cancel) {
		cancel = true;
	}
	else {
		cancel = false;
		elapsed = 0;
		process();
	}
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

jQuery.fn.removeAttributes = function() {
  return this.each(function() {
    var attributes = $.map(this.attributes, function(item) {
      return item.name;
    });
    var img = $(this);
    $.each(attributes, function(i, item) {
    img.removeAttr(item);
    });
  });
}
