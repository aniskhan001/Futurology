// var myjson;
// $.getJSON("https://www.reddit.com/r/Futurology/top.json", function(json){
//     myjson = json;
// });


// console.log(myjson);

var xhReq = new XMLHttpRequest();
xhReq.open("GET", 'https://www.reddit.com/r/Futurology/top.json', false);
xhReq.send(null);
var jsonObject = JSON.parse(xhReq.responseText);
var post_list = jsonObject.data.children;
console.log(post_list);
