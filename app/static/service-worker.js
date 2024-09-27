const CACHE_NAME = 'flask-pwa-cache-v1';
const urlsToCache = [
  '/',
  '/static/manifest.json'
];

// Cài đặt Service Worker và lưu trữ các tài nguyên trong bộ nhớ cache
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Kích hoạt Service Worker và loại bỏ các cache cũ
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (!cacheWhitelist.includes(cacheName)) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Bắt các yêu cầu mạng và phục vụ từ cache nếu có
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Trả về từ cache nếu có
        if (response) {
          return response;
        }

        // Clone yêu cầu để có thể sử dụng nó trong cả cache và mạng
        const fetchRequest = event.request.clone();

        return fetch(fetchRequest).then(
          networkResponse => {
            // Kiểm tra xem phản hồi có hợp lệ không
            if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
              return networkResponse;
            }

            // Clone phản hồi để có thể sử dụng nó trong cache và trả về cho trình duyệt
            const responseToCache = networkResponse.clone();

            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseToCache);
              });

            return networkResponse;
          }
        );
      })
  );
});