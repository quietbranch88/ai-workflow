# Python Pitfalls — what AI keeps getting wrong (Django-flavored)

## Mutable default arguments

```python
# WRONG — list shared across calls
def add_item(item, items=[]):
    items.append(item)
    return items

# RIGHT
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## `==` vs `is`

- `is` checks identity (same object in memory).
- Use `is` only for `None` and other real singletons.
- Do not write `x is True` or `x is False`. Use `if x:` / `if not x:`.
- Everything else uses `==`.

## Type hints actually help — use them

- Add type hints to function signatures.
- Run `mypy` or `pyright` in CI.
- AI generates better code when types are explicit.

## Async pitfalls

- `await` inside non-async function → `SyntaxError`.
- Forgetting `await` on a coroutine → "coroutine was never awaited" warning, silently broken.
- Mixing a sync ORM call into async code needs `sync_to_async`. QuerySet also has async methods such as `aget` and `acreate`; wrapping the sync call is not that path.

## Django ORM

- **`.get()` raises `DoesNotExist`.** Use `.filter().first()` or `try/except`.
- **N+1 queries** — always use `select_related` / `prefetch_related` for FK / M2M when iterating.
- `Model.save()` triggers signals; bulk operations bypass them.
- `bulk_create` and `bulk_update` do not call `save()` and do not send signals. `bulk_create` still runs `field.pre_save` on insert, so `auto_now_add` is set. `bulk_update` does not run `pre_save`, so `auto_now` stays unchanged.
- Migrations are NOT free: adding a NOT NULL column on a big table can lock writes. Always do it in two steps (nullable + backfill, then NOT NULL).
- **Never trust user input through to a `.raw()` SQL** — parameterize.

## Django settings

- `DEBUG = True` in production is a security disaster.
- `SECRET_KEY` from env, never committed.
- `ALLOWED_HOSTS` must be set in production.
- Django does not pool connections by default. `CONN_MAX_AGE` keeps one persistent connection for a thread; it is not a pool. Use a real pool such as pgbouncer, and set `CONN_MAX_AGE` to `0` when the pool owns connection lifetime.

## Celery

- Tasks must be idempotent. A task runs once unless it calls `self.retry()`, sets `autoretry_for`, or the broker redelivers it.
- Don't pass large objects (querysets, files) as task args — pass IDs.
- `bind=True` if you need `self.retry()`.
- Result backend has TTL — don't rely on results being there forever.

## Testing

- Use `pytest-django` for Django tests.
- `@pytest.mark.django_db` for tests that touch the DB.
- Factory Boy or `model_bakery` > `Model.objects.create()` for test fixtures.
- Mock external HTTP with `responses` or `pytest-httpx`, not `unittest.mock` raw.
- Property-based testing: `hypothesis` library.

## Dependency hygiene

- `uv` (or `poetry`) for venv + locking. Avoid bare `pip install` for project deps.
- Pin direct deps; lock indirect via `uv.lock`.
- Audit with `pip-audit` for CVEs.

## Logging & secrets

- NEVER `print()` in production code — use `logging`.
- NEVER log full request bodies (PII leak).
- NEVER format strings with secrets: `f"key={api_key}"` ends up in tracebacks.

## Performance traps

- String concatenation in loops → use `"".join()`.
- `list.append()` in tight loops can dominate — pre-size if length is known.
- JSON serialization with stdlib `json` is slow for large payloads — use `orjson`.

## Pre-commit checklist

- [ ] `ruff check .` passes
- [ ] `mypy` (or `pyright`) passes
- [ ] `pytest` passes
- [ ] No `print()` statements in non-script code
- [ ] No hardcoded secrets / API keys
- [ ] New deps verified
