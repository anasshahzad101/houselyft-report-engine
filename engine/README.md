# Report Engine (port pending)

The feasibility report generator gets ported here from Claude project sessions:

- `zoning/` - property_lookup_v2 nine-city GTA zoning engine
- `imagery/` - aerial_imagery module (municipal open-data endpoints, blank-tile validation)
- `templates/` - master report template + city transform scripts
- `generate.py` - single entrypoint: address in, branded PDF out

Until the port lands, `src/run_report.py` stops at the engine step with a clear error.
