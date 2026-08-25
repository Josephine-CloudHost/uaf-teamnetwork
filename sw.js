// Firebase Cloud Messaging service worker.
// This file MUST live at the site root next to index.html (e.g. alongside your
// GitHub Pages index.html) and be registered as 'sw.js' (a relative path) so it
// works whether the site is served at the domain root or from a project subpath
// like username.github.io/repo/.
//
// Without this file, registerPushNotifications() in index.html has nothing to
// register, messaging.getToken() fails, and no background push notifications
// can ever be delivered — the app only sees messages while it's open and in
// the foreground.

importScripts('https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.8.0/firebase-messaging-compat.js');

firebase.initializeApp({
  apiKey: "AIzaSyD3IhrkjB-cRzYZVBscwkYehPd0VS00YFw",
  authDomain: "uaf-team-network.firebaseapp.com",
  projectId: "uaf-team-network",
  storageBucket: "uaf-team-network.firebasestorage.app",
  messagingSenderId: "936656734962",
  appId: "1:936656734962:web:84267c3b78809822bade6b",
  measurementId: "G-9CNP5RP4Y1"
});

const messaging = firebase.messaging();

// Shows a native OS notification when a push arrives while the app tab is
// closed or backgrounded.
messaging.onBackgroundMessage((payload) => {
  const title = (payload.notification && payload.notification.title) || 'UAF Team Network';
  const body = (payload.notification && payload.notification.body) || 'New notification';
  self.registration.showNotification(title, {
    body: body,
    tag: 'uaf-team-network' // collapses rapid-fire notifications into one instead of stacking dozens
  });
});

// Tapping the notification focuses an existing app tab if one is open, or
// opens a new one.
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((windowClients) => {
      for (const client of windowClients) {
        if ('focus' in client) return client.focus();
      }
      if (clients.openWindow) return clients.openWindow('./');
    })
  );
});
