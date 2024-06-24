# sessionai-assignment

Approach : 
- To obatin continuos logs monitoring from remote servers to a centraliszed monitoriting-alerting-visualtion dashboard I have used GRAFANA <- lOKI <- PROMTAIL
- Here in this sample I have used containers as remote servers to mimic the actual scenario. All of there containers will have promtail scarping data { here log files /var/log/*log } to LOKI as a job named varlogs using this file : [promtail-config.yaml](https://github.com/OjasKhamkar/sessionai-assignment/blob/main/promtail-config.yaml)
- Loki is a log aggregation system in Grafana that stores and queries logs from applications and infrastructure. The configuration for this is : [loki-config.yaml](https://github.com/OjasKhamkar/sessionai-assignment/blob/main/loki-config.yaml)
- Finally I have hosted Grafana on my local ubuntu machine, To mimic a centralised VM which will be used for end to end workflow.



Below is my personalised dashboard that can be attained using [personalized-dashboard](https://github.com/OjasKhamkar/sessionai-assignment/blob/main/grafana-dashboard.json) 

![ojas-sessionai-dashboard](https://github.com/OjasKhamkar/sessionai-assignment/assets/58805468/de9f7463-392c-4ae1-a635-5d6d450d246b)

LOKI 's raw data aggregration :
![loki](https://github.com/OjasKhamkar/sessionai-assignment/assets/58805468/e5781e5a-c7bf-452d-967b-42b64b23007d)
