# Model behavior and limitations

## Intended use

The PulseOps model prioritizes assets for maintenance review. It supports, but does not replace, decisions by qualified engineers.

## Inputs

The model evaluates vibration, temperature, rotational speed, asset type, and recent trends. Missing, stale, or incorrectly scaled telemetry reduces confidence.

## Confidence guidance

| Confidence | Meaning | Recommended handling |
|---|---|---|
| 0.80-1.00 | Request is similar to validated operating conditions | Review normal risk controls |
| 0.60-0.79 | Some conditions differ from validated data | Require engineer review |
| Below 0.60 | Prediction may be unreliable | Treat as insufficient evidence and inspect data quality |

## Known limitations

- The model has not been validated for equipment types absent from the supported-assets list.
- Recent repairs or sensor replacement can create temporary drift.
- A low-risk response does not prove that an asset is safe.
- Predictions depend on sensor calibration and time synchronization.
- The model should not trigger autonomous shutdowns or safety actions.

## Monitoring and drift

Track confidence distribution, prediction volume, engineer overrides, false alarms, and missed failures. Revalidate the model when the operating environment, sensor configuration, or maintenance policy changes.

## Documentation QA checklist

1. Verify examples against the current schema.
2. Confirm units and time windows with engineering.
3. Separate observed facts from model estimates.
4. State required human decisions explicitly.
5. Review limitations at every model release.
