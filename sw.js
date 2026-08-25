// Service worker: handles background push notifications only.
// Token generation happens in the page (index.html), not here —
// a service worker has no access to the logged-in user's email.

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

// Handle notifications that arrive while the app is in the background/closed
messaging.onBackgroundMessage((payload) => {
  const notificationTitle = payload.notification?.title || "UAF Team Network Alert";
  const notificationOptions = {
    body: payload.notification?.body || "New message received.",
    icon: "/icon-192.png",
    data: payload.data || {}
  };
  self.registration.showNotification(notificationTitle, notificationOptions);
});
