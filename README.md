# Network-Security-Synthetic-Data
Data            |Accuracy|Precision|Recall|F1-Score|
----------------|--------|---------|------|--------|
Real            |98.85%  |98.93%   |98.85%|98.88%  |
CTGAN           |95.75%  |96.36%   |95.75%|96.02%  |
TVAE            |96.95%  |96.43%   |96.95%|96.27%  |
Gaussian Copula |96.30%  |96.44%   |96.30%|94.53%  |


### Real Data
|            |Predicted 0|Predicted 1|
-------------|-----------|------------
|**Actual 0**|1909       |16         |
|**Actual 1**|7          |68         |

### CTGAN Data
|            |Predicted 0|Predicted 1|
-------------|-----------|------------
|**Actual 0**|1871       |54         |
|**Actual 1**|31         |44         |

### TVAE Data
|            |Predicted 0|Predicted 1|
-------------|-----------|------------
|**Actual 0**|1918       |7          |
|**Actual 1**|54         |21         |

### Gaussian Copula Data
|            |Predicted 0|Predicted 1|
-------------|-----------|------------
|**Actual 0**|1925       |0          |
|**Actual 0**|74         |1          |
