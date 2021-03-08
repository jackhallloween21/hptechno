//Node.js 10.14.0
//Plain Javascript and Node.js is supported
// html/css is not supported here 

let roses = {
  areRed:true,
};
let violets ={
  areBlue:true,
};
function createpoem(thirdline, fourthline)
{
  if (roses.areRed&&violets.areBlue)
  {
    console.log('Roses are red');
    console.log('violets are blue');
    console.log(thirdline);
    console.log(fourthline);
  }
}
createpoem('coding is awesome','And so are You! :-)');
