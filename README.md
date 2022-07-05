# Google Search Console Exporter
Export Google Search Data via the **Google Search Console API** to **BigQuery**.
## Flowchart
```mermaid
graph LR;
    a((timer)) --> b[extract] --> c[load];
```