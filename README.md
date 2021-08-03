# analyze-google-analytics

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets for Google Analytics. These datasets are automatically added to your Matatika workspace when you initialize a Google Analytics pipeline.

Files:
- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

### Adding this file bundle to your own Meltano project

Add plugin to `discovery.yml`:
```yaml
files:
- name: analyze-google-analytics
  namespace: tap_google_analytics
  repo: https://github.com/Matatika/analyze-google-analytics
  pip_url: git+https://github.com/Matatika/analyze-google-analytics.git
```

Add plugin to your Meltano project:
```bash
# Add only the file bundle
meltano add files analyze-google-analytics

# Add the file bundle as a related plugin through adding the Google Analytics extractor
meltano add extractor --include-related tap-google-analytics
```
