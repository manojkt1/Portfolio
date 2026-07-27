# Get started with the PulseOps Prediction API

> PulseOps is a fictional product created as a technical-writing portfolio sample.

Use the Prediction API to submit recent equipment telemetry and receive a failure-risk assessment for the next 72 hours.

## Before you begin

You need:

- an API key with the `predictions:write` scope;
- a stable equipment identifier;
- at least 30 minutes of timestamped telemetry;
- vibration, temperature, and rotational-speed measurements in the documented units.

Store API keys in a secret manager. Do not commit them to source control.

## 1. Send an inference request

```bash
curl --request POST \
  --url https://api.pulseops.example/v1/predictions \
  --header "Authorization: Bearer $PULSEOPS_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: 91f2c230-7bd5-4bd1-b2bc-e33847fd30a1" \
  --data '{
    "asset_id": "pump-17",
    "observed_at": "2026-07-25T08:30:00Z",
    "telemetry": {
      "vibration_mm_s": 8.4,
      "temperature_c": 92.1,
      "rotational_speed_rpm": 2975
    }
  }'
```

## 2. Interpret the response

```json
{
  "prediction_id": "pred_01J3Q6X4G8M2",
  "asset_id": "pump-17",
  "risk_level": "high",
  "failure_probability": 0.82,
  "confidence": 0.76,
  "prediction_window_hours": 72,
  "signals": ["vibration_above_baseline", "temperature_trend_increasing"],
  "recommended_action": "Inspect bearings within 8 hours.",
  "requires_human_review": true
}
```

- `failure_probability` estimates failure risk within the prediction window. It is not a guarantee.
- `confidence` describes how closely the request resembles data used to validate the model.
- `requires_human_review` is `true` for high-risk responses and low-confidence predictions.

## 3. Implement a safe fallback

Do not automatically stop equipment using the prediction alone. Route high-risk results to a qualified maintenance engineer and combine the result with operating context, inspections, and existing safety procedures.

## Next steps

- Review [model behavior and limitations](model-behavior.md).
- Implement error handling using the [error reference](errors.md).
- Explore the complete [OpenAPI definition](openapi.yaml).
