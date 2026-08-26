#!/usr/bin/env node
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { once } from 'node:events';

const port = 4174;
const base = `http://127.0.0.1:${port}`;
const server = spawn('python3', ['-m', 'http.server', String(port), '--bind', '127.0.0.1', '--directory', 'public'], {
  cwd: new URL('..', import.meta.url).pathname,
  stdio: ['ignore', 'ignore', 'pipe'],
});

async function ready() {
  for (let i = 0; i < 50; i++) {
    try {
      const response = await fetch(`${base}/`);
      if (response.ok && (await response.text()).includes('DahlmannOnline Blog')) return;
    } catch {}
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  throw new Error('blog preview did not become ready');
}

try {
  await ready();
  const child = spawn(process.execPath, ['tests/browser-smoke.mjs', base], {
    cwd: new URL('..', import.meta.url).pathname,
    stdio: 'inherit',
  });
  const [code] = await once(child, 'exit');
  assert.equal(code, 0, `browser smoke exited ${code}`);
} finally {
  server.kill('SIGTERM');
  if (server.exitCode === null) await Promise.race([once(server, 'exit'), new Promise(r => setTimeout(r, 1000))]);
}
