# Error reference

Errors use a stable `code`, a readable `message`, a `request_id`, and optional field-level details.

```json
{
  "error": {
    "code": "TELEMETRY_OUT_OF_RANGE",
    "message": "vibration_mm_s must be between 0 and 50.",
    "request_id": "req_01J3Q7B7K4W9",
    "field": "telemetry.vibration_mm_s"
  }
}
```

| HTTP status | Code | Cause | Resolution |
|---|---|---|---|
| 400 | `INVALID_REQUEST` | JSON or a required field is invalid | Correct the field identified in the response |
| 401 | `INVALID_API_KEY` | Key is missing, expired, or revoked | Rotate the key and retry |
| 403 | `INSUFFICIENT_SCOPE` | Key lacks `predictions:write` | Request the required scope |
| 409 | `IDEMPOTENCY_CONFLICT` | Key was reused with a different body | Generate a new idempotency key |
| 422 | `TELEMETRY_OUT_OF_RANGE` | A value falls outside supported limits | Verify sensor units and calibration |
| 429 | `RATE_LIMITED` | Request quota was exceeded | Wait for `Retry-After` and retry with backoff |
| 503 | `MODEL_UNAVAILABLE` | Model deployment is temporarily unavailable | Use the documented fallback and retry later |
