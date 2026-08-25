self.addEventListener('push', function(event) {
  const data = event.data ? event.data.json() : {};
  const title = data.title || "UAF Team Network Alert";
  const options = {
    body: data.body || "New event or message received.",
    icon: "icon-192.png",
    badge: "icon-192.png",
    data: {
      targetTab: data.targetTab || 'feed',
      targetId: data.targetId || ''
    }
  };

  event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', function(event) {
  event.notification.close();
  event.waitUntil(
    clients.matchAll({ type: 'window' }).then(windowClients => {
      for (let client of windowClients) {
        if (client.url && 'focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow('/');
      }
    })
  );
});
