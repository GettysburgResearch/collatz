'use strict';const fs=require('fs');const basis=fs.readFileSync(require('path').join(__dirname,'lib','qpoly-basis.js'),'utf8').split('const maxU =')[0];const peel=fs.readFileSync(require('path').join(__dirname,'lib','cyclotomic-peeling-basis.js'),'utf8'),h=peel.slice(peel.indexOf('function modNorm'),peel.indexOf('const maxU2'));
const z=String.raw`
const maxU=Number(process.argv[2]||18),maxM=Number(process.argv[3]||160);let bad=[],zeros=[],hist={};
for(let u=1;u<=maxU;u++){const P=Q(u);for(let m=2;m<=maxM;m++)if(m%3!==0&&3*m>2*u+1&&phi(3*m)<=P.length-1){const v=multiplicityMod(P,cyclotomic(m),3);hist[v]=(hist[v]||0)+1;if(v)zeros.push({u,m,v});if(v>=2)bad.push({u,m,L:3*m,v});}}
console.log(JSON.stringify({hist,zeros:zeros.slice(0,300),bad:bad.slice(0,200),count:bad.length},null,2));
`;Function('process',basis+'\n'+h+'\n'+z)(process);


