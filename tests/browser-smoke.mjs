#!/usr/bin/env node
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const AxeBuilder = require('@axe-core/playwright').default;

const base = (process.argv[2] || 'http://127.0.0.1:4174').replace(/\/$/, '');
const browser = await chromium.launch({ headless: true });
const results = [];

try {
  for (const viewport of [
    { name: 'desktop', width: 1440, height: 1000 },
    { name: 'mobile', width: 390, height: 844 },
  ]) {
    const context = await browser.newContext({ viewport });
    const page = await context.newPage();
    const consoleErrors = [];
    page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
    page.on('pageerror', error => consoleErrors.push(error.message));

    for (const route of ['/', '/anleitungen/', '/suche/', '/impressum/', '/datenschutz/', '/posts/bedeutung-von-passwortmanagern/']) {
      const response = await page.goto(`${base}${route}`, { waitUntil: 'networkidle' });
      assert.equal(response.status(), 200, `${viewport.name} ${route} status`);
      assert.match(await page.title(), /DahlmannOnline Blog/, `${viewport.name} ${route} wrong site`);
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      assert.equal(overflow, 0, `${viewport.name} ${route} horizontal overflow`);
      const axe = await new AxeBuilder({ page }).analyze();
      const serious = axe.violations.filter(v => ['serious', 'critical'].includes(v.impact));
      assert.deepEqual(serious.map(v => v.id), [], `${viewport.name} ${route} axe serious/critical`);
    }

    await page.goto(`${base}/posts/bedeutung-von-passwortmanagern/`, { waitUntil: 'networkidle' });
    assert.equal(await page.locator('iframe').count(), 0, 'external iframe must be opt-in');
    assert.equal(await page.locator('script[src="https://giscus.app/client.js"]').count(), 0, 'Giscus must not load initially');
    assert.ok(await page.getByRole('button', { name: /YouTube-Video laden/ }).count(), 'YouTube opt-in button missing');
    assert.ok(await page.getByRole('button', { name: /Kommentare laden/ }).count(), 'Giscus opt-in button missing');

    await page.goto(`${base}/suche/`, { waitUntil: 'networkidle' });
    const input = page.locator('.pagefind-ui__search-input');
    await input.waitFor();
    const searchResults = {};
    for (const term of ['Passwortmanager', 'Excel', 'Schule']) {
      await input.fill(term);
      await page.waitForFunction(
        (expected) => Array.from(document.querySelectorAll('.pagefind-ui__result-link')).some(node => node.textContent.includes(expected)),
        term,
        { timeout: 8000 }
      );
      const urls = await page.locator('.pagefind-ui__result-link').evaluateAll(nodes => nodes.map(n => n.getAttribute('href')));
      assert.ok(urls.length > 0, `${term} should return real hits`);
      const feedback = await page.locator('.pagefind-ui__search-feedback, .pagefind-ui__message').first().textContent().catch(() => '');
      assert.ok(!/Keine Ergebnisse/.test(feedback), `${term} reported no results`);
      assert.ok(urls.every(url => url.includes('/posts/')), `${term} returned non-post URL: ${urls.join(', ')}`);
      searchResults[term] = urls.length;
    }
    await input.fill('qxvplmnrst');
    await page.waitForFunction(() => /Keine Ergebnisse/.test(document.body.innerText));
    assert.equal(await page.locator('.pagefind-ui__result').count(), 0, 'nonsense query should have no hits');
    searchResults.qxvplmnrst = 0;

    assert.deepEqual(consoleErrors, [], `${viewport.name} console/page errors`);
    results.push({ viewport: viewport.name, searchResults });
    await page.close();
  }
  console.log(`browser-smoke: PASS ${JSON.stringify(results)}`);
} finally {
  await browser.close();
}
