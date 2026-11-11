import test from 'node:test';import assert from 'node:assert/strict';import {readFileSync} from 'node:fs';import {rank,explain} from '../demo/logic.mjs';
const docs=JSON.parse(readFileSync(new URL('../data/conocimiento.json',import.meta.url))).documentos;
test('recuperación léxica del envío',()=>assert.equal(rank('envíos Lima',docs)[0].id,'DOC-02'));
test('abstención para consulta fuera de corpus',()=>assert.equal(explain('xylophone quasar',docs).hits.length,0));
test('sin HTML inyectable en lógica',()=>assert.equal(typeof explain('<script>alert(1)</script>',docs).answer,'string'));
