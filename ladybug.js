let arc =d3.arc(_);
let ladybug = svg.append('g').attr('transform','translate(150,220');

let body = ladybug.append('circle').attr('r',50).attr('fill', 'black');

let head = ladybug.append('circle').attr('r',20).attr('fill', 'black').attr('cy', -60);

let leftWing = ladybug.append('path').attr( 'd', arc({

innerRadius:0,

outerRadius: 55,

startAngle: -Math.PI * 0.95,

endAngle: 0,
_:_

},__)).attr('fill', 'red');

let rightWing = ladybug.append('path').attr( 'd', arc({

innerRadius: 0,

outerRadius: 55,

startAngle: Math.PI * 0.95,

endAngle: 0,
_:_
},__)).attr('fill', 'red');

let leftAntannae = ladybug.append('line').attr('x1', - 5 ).attr('y1', -60).attr('x2',15).attr('y2', -100).attr('stroke', 'black').attr('stroke-width', 3);

let rightAntennae =ladybug.append('line').attr('x1', 5).attr('yl', -60).attr('X2', 15 ).attr('y2', -100).attr('stroke', 'black').attr('stroke-width',3);

function addSpots(amount,__){

for (let i = 0; i < amount; i++) {

ladybug.append('circle').attr('r', 10).

attr('cx', 40 * Math.cos((i - 1 ) * 2 * Math.PI / amount,__)).attr('cy',40*Math.sin((i-1) * 2 * Math.PI / amount,__)).attr('fill', 'black');}
 };

addSpots( 6 );

ladybug.transition().attr('transform', 'translate(150, 100)').duration (3000).ease(d3.easeQuadout);