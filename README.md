# dPCA
This repository contains the distributed PCA code written for the old coinstac simulator (v2.3). It contains the following files:
1. dpca_local.py - for computing the local PCA on local data and sending the proxy data matrix to the master.
2. dpca_master.py - for aggregation of the proxy data matrix sent by local sites and releasing the top-K principal components
3. computation.js - computation specification JavaScript file
4. declaration.js - declaration file specifying the local site names,  JavaScript file
