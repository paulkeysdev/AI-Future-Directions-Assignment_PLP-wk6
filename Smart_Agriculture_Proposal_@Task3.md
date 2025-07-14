# Smart Agriculture Proposal (Task 3)

## Sensors Required
1. Soil moisture sensors
2. Ambient temperature/humidity sensors
3. Multispectral cameras (NDVI)
4. Weather station (rainfall, wind,sunshine)

## AI Model Architecture
- Input: Sensor time-series data + satellite imagery
- Model: LSTM + CNN hybrid
- Output: Yield prediction with confidence intervals

## Data Flow Diagram
```
[IoT Devices] → [Edge Gateway] → [Cloud API] → [AI Model] → [Farmer Dashboard]
            (Local processing)    (Heavy compute)
``` 
