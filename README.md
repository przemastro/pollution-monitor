# PollutionMonitor
[![GitHub issues](https://img.shields.io/github/issues/przemastro/pollution-monitor)](https://github.com/przemastro/pollution-monitor/issues)
[![GitHub forks](https://img.shields.io/github/forks/przemastro/pollution-monitor)](https://github.com/przemastro/pollution-monitor/network)
[![GitHub stars](https://img.shields.io/github/stars/przemastro/pollution-monitor)](https://github.com/przemastro/pollution-monitor/stargazers)
[![Python version](https://img.shields.io/badge/Python-2.7.x-%233572A5)](https://github.com/przemastro/performance-testing-training-polish)

![Dashboard](https://github.com/przemastro/pollution-monitor/blob/master/plot.png)

![Dashboard](https://github.com/przemastro/pollution-monitor/blob/master/Description.PNG)

# Features
Data gathered from https://aqicn.org. Mostly Air Quality Index value for 7 cities: Poznan(Poland), Cordoba(Spain), Liverpool(UK), Nijmegen(Netherlands), Hanover(Germany), Toulouse(France) and Gent(Belgium). The criteria was simple: Similar size, similar number of citizens, similar distance from the coast.
For the purpose of this investigation I will be using: SQL Server as data storage, python requests to get data from https://aqicn.org 
and plotly library to plot reults.

# Installation

1. Python, pip and libraries plotly, pysql
2. SQL Server

# Run

python pollutionMonitor.py

