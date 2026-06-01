# Change-of-coordinate-system-from-MCP-to-centre-of-STN

This repository contains the implementation of a coordinate transformation method used to convert deep brain stimulation (DBS) electrode contact coordinates from the mid-commissural point (MCP) reference frame to a subthalamic nucleus (STN)-centered coordinate system.

Description

The transformation pipeline includes:

Translation of coordinates from MCP-referenced space to the STN center
Rotation of coordinates based on the anatomical orientation of the STN
Calculation of Euclidean distance from the STN center


This code was developed as part of a research study on DBS electrode localization and prediction.


# Requirements

This code was developed and tested in Google Colab.

Required Python libraries:

numpy
pandas
matplotlib
plotly
scikit-learn
scipy
# How to Run
Open the notebook in Google Colab.
Upload the required dataset.
Run all cells sequentially.
The notebook will generate transformed coordinates and visualizations.
# Data Availability

Due to clinical and patient privacy restrictions, the original dataset cannot be publicly shared. The repository contains code for reproducing the analysis pipeline.
The data will be made available upon request, subject to a reasonable justification
