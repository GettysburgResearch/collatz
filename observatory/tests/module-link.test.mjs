/** Link the actual ES-module graphs without a DOM or flattening imports. */
import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const webRoot=fileURLToPath(new URL('../web/',import.meta.url));

test('new and classic real ES-module graphs have compatible imports/exports',()=>{
  const source=`
    import vm from 'node:vm';
    import fs from 'node:fs';
    import path from 'node:path';
    const modules=new Map();
    function get(filename){
      if(!modules.has(filename)) modules.set(filename,new vm.SourceTextModule(fs.readFileSync(filename,'utf8'),{identifier:filename}));
      return modules.get(filename);
    }
    for(const root of ['lab.mjs','app.mjs']) {
      const module=get(path.resolve(root));
      await module.link((specifier,parent)=>get(path.resolve(path.dirname(parent.identifier),specifier)));
      if(module.status!=='linked') throw new Error('Module graph failed to link.');
    }
    console.log('LINKED');
  `;
  const output=execFileSync(process.execPath,['--experimental-vm-modules','--input-type=module','-e',source],{cwd:webRoot,encoding:'utf8',stdio:['pipe','pipe','pipe']});
  assert.equal(output.trim(),'LINKED');
});
