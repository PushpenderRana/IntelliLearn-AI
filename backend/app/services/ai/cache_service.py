import time
import uuid
import threading
from typing import Any, Optional


class CacheService:
    """In-memory TTL cache. Swap internals for Redis later, same interface."""

    def __init__(self, ttl_seconds: int = 1800):
        self.ttl = ttl_seconds
        self._store: dict[str, dict] = {}
        self._lock = threading.Lock()

    def _purge_expired(self):
        now = time.time()
        expired = [k for k, v in self._store.items() if v["expires_at"] < now]
        for k in expired:
            self._store.pop(k, None)

    def create(self, data: Any) -> str:
        quiz_id = str(uuid.uuid4())
        with self._lock:
            self._purge_expired()
            self._store[quiz_id] = {"data": data, "expires_at": time.time() + self.ttl}
        return quiz_id

    def get(self, quiz_id: str) -> Optional[Any]:
        with self._lock:
            self._purge_expired()
            entry = self._store.get(quiz_id)
            return entry["data"] if entry else None

    def delete(self, quiz_id: str) -> None:
        with self._lock:
            self._store.pop(quiz_id, None)


# Singleton used across app. TTL = 30 min per spec.
cache_service = CacheService(ttl_seconds=1800)

# --- Redis swap-in (optional) ---
# import redis, json
# class RedisCacheService:
#     def __init__(self, url="redis://localhost:6379/0", ttl_seconds=1800):
#         self.r = redis.from_url(url)
#         self.ttl = ttl_seconds
#     def create(self, data):
#         quiz_id = str(uuid.uuid4())
#         self.r.setex(quiz_id, self.ttl, json.dumps(data))
#         return quiz_id
#     def get(self, quiz_id):
#         raw = self.r.get(quiz_id)
#         return json.loads(raw) if raw else None
#     def delete(self, quiz_id):
#         self.r.delete(quiz_id)