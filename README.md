<h1 align="center"> Pandas ETL Challenge </h1>

![pandas logo](https://user-images.githubusercontent.com/93624837/203309606-0b034b69-c40e-4ee6-9029-019676950f1c.jpg)

![badge release date](https://img.shields.io/badge/release%20date-November%2F2022-blue)

### TOPICS
* [Files](#files)
* [Code Description](#code-description)
* [My Comments](#my-comments)
* [Author](#author)


## Files

<p align="justify">
<b>• exercise.py</b>: the original Python script.

<b>• source_data.csv</b>: the original input CSV file.

<b>• main.py</b>: improved Python script (based on the original script).

<b>• processed_data.py</b>: the output CSV file (created by main.py).
</p>


## Code Description

<p align="justify">
This is a ETL pipeline created using Python and his library Pandas. This script ("main.py") it's a improved version of the original script ("exercise.py"):  it's read a CSV file ("source_data.csv"), then the data contained in this file are processed and in the end, a new CSV file ("processed_data.csv") it's created. In order to run, this script ("main.py") and the source file ("source_data.csv") needs to be in the same folder.
</p>

## My Comments

<p align="justify">
With the small information who was given about this task, I decide to keep some aspects of the original script (like use only a few libraries, keep all the code in a single file etc.) and use it as a guidelines when I wrote this code.

In the code, I try to keep it as clean, simple and readable (human friendly) as possible. 

In my humble opinion (based on my professional experience), the best code (besides of course, of all the technical aspects about write a good code)  it's the code who fits the business process and needs. For example: I could use Great Expectations Python library to validate the data from the source CSV file ("source_data.csv") in order to improve the data integrity, but I assumed that this would be not necessary, based on the steps that was used in the original script ("exercise.py").

In order to improve this script even more and provides even better quality data, it's very important to deep understand the business and IT process about this required data. Once we have this, we can write the code using the best methods and practices, this also allow us to avoid multiple errors scenarios, since we can anticipated their and work in their solutions on a approach who minimize the risks. Without this specific knowledge, sometimes it's better keep the code simple and functional than use <i>"a cannon to kill an ant"</i> who would use more computational resources than the task really need.
</p>


## Author

<p align="justify"> Gustavo de Souza Pessanha da Costa. </p>


