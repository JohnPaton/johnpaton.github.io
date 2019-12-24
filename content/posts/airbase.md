title: Introducing airbase: A Python client for the European Air Quality e-Reporting Database
slug: airbase
date: 2019-12-30 18:00:00 UTC+01:00
tags: python, open source, data, timeseries
category: 
cover: images/airbase-screenshot.png
link: 
status: draft
description:
type: text
author: John Paton
summary: The European Environment Agency (EEA) provides a selection of datasets about air quality in Europe. The data is available for download at [the portal](http://discomap.eea.europa.eu/map/fme/AirQualityExport.htm), but the interface makes it a bit time consuming to do bulk downloads. Hence, an easy Python-based interface.

As part of its open data initiatives, the [European Environment Agency (EEA)](https://www.eea.europa.eu/) provides a selection of datasets about air quality in Europe, collectively known as the [Air Quality e-Reporting](https://www.eea.europa.eu/data-and-maps/data/aqereporting-8#tab-european-data) database. The richest subset of this data is the air quality time series data. There are 2 subsets: E1a, which is cleaner and more validated, and E2a, which is more up to date. This is an important dataset for climate research, as well as a great source for data scientists who are looking for some non-trivial real world data to practice on (when combined with the measurement station metadata, you have both geodata and timeseries).

The one major obstacle to using this data is the download interface (a.k.a. "the portal"), which is very cumbersome. First you need to navigate to the [download page](http://discomap.eea.europa.eu/map/fme/AirQualityExport.htm) and select the parameters of the dataset you want to download, like the pollutant of interest, the location, and the time span:

![Airbase download form](/images/airbase-download-form.png)

The form constructs a URL with query parameters matching what you've selected in the form (this was my first hint that this should be easy to automate). Once you hit the "Download" button, you would expect that it would download the dataset, but that would of course be too easy. If you hit the button [for the parameters I've filled in](https://fme.discomap.eea.europa.eu/fmedatastreaming/AirQualityDownload/AQData_Extract.fmw?CountryCode=NL&CityName=&Pollutant=46&Year_from=2014&Year_to=2017&Station=&Samplingpoint=&Source=E1a&Output=HTML&UpdateDate=&TimeCoverage=Year) you're greeted with a list of links to various CSV files to individually click on and download yourself. 

![Airbase CSV links](/images/airbase-links.png)

For this particular query this isn't _too_ bad, but if you want to query many types of pollutant or a bigger group of countries, this is going to cost you some serious time. 

# A better way

To make this process easier, I developed [`airbase`: an easy Python client](https://airbase.readthedocs.io/en/latest/) for accessing the data (this database was [formerly known](https://www.eea.europa.eu/data-and-maps/data/airbase-the-european-air-quality-database-7) as AirBase, and I thought it was a catchy name). It started off as a script to help a friend of mine who is in climate research, and I realized with a bit of cleanup it might be useful to other people as well. It's available on PyPI, so to install you can simply 

```bash
$ pip install airbase
```

To start downloading your dataset, import the package and initialize the client:

```python
>>> import airbase
>>> client = airbase.AirbaseClient()
```

The client helps you to construct your request, and does some validation for you, like checking that the pollutant you want is available in the countries you're asking for. It does this by downloading some files from the portal, so this requires an internet connection.

Kind of like using the portal, but more conveniently, you next construct the parameters of the dataset you're looking for:

```python
>>> request = client.request(country="NL", pl="NO3", year_from=2014, year_to=2017)
```
 
If you don't include a parameter, the client will construct a request for all possible values (so you can just user `client.request()` to get the whole dataset).

With your request constructed, all that's left to do is to choose how you want to download the data. You can choose to either [`download_to_directory()`](https://airbase.readthedocs.io/en/latest/airbase.html#airbase.AirbaseRequest.download_to_directory) to get all those CSVs individually, or you can [`download_to_file()`](https://airbase.readthedocs.io/en/latest/airbase.html#airbase.AirbaseRequest.download_to_file) to concatenate them into one big CSV. Either way, the request object will first contact the portal to get the links to all the CSVs you need, and then start downloading them as instructed. Of course, you can follow the progress with nice progress bars.

```python
>>> request.download_to_directory("./data")
Generating CSV download links...
100%|██████████████████████████| 1/1 [00:03<00:00,  3.14s/it]
Generated 16 CSV links ready for downloading
Downloading CSVs to ./data...
100%|██████████████████████████| 16/16 [00:03<00:00,  5.34it/s]
```

If you want to update your dataset later (e.g. getting the last week's worth of data), `download_to_directory()` will automatically skip downloading most of the files that are already there. 

Hunting for correlations between locations? Make sure to download the metadata file that contains the locations and other properties of the measurement stations that supply the data:

```python
>>> client.download_metadata("./data/metadata.csv")
Writing metadata to ./data/metadata.csv...
```

Full documentation is availble on [ReadTheDocs](https://airbase.readthedocs.io/en/latest), and of course the whole package is [open sourced on GitHub](https://github.com/johnpaton/airbase) too. I know at least a handful of people have used the package, including [one confirmed publication](https://www.atmos-chem-phys.net/19/11821/2019) (by my friend who I made the original script for), which is very cool!

Have you used `airbase` in your research or learning? Let me know! I'd love to hear about it! 



