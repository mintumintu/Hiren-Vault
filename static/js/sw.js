(global => {
  'use strict';

  // Load the sw-toolbox library.
  importScripts('sw-toolbox.js');
  
  // Ensure that our service worker takes control of the page as soon as possible.
  global.addEventListener('install', event => event.waitUntil(global.skipWaiting()));
  global.addEventListener('activate', event => event.waitUntil(global.clients.claim()));
})(self);

toolbox.router.get('/(.*)', global.toolbox.cacheFirst, {
  origin: /static/
});