# forecastguy
<h5>Forecastguy is CLI developed for demostration. It is not production ready or fully optimized. Time was a factor while developing this tool. Hope to make it better, in coming days. Beautiful code was not the target. Code complies with pep8 standards. In future a separate JSON API will be developed for carrying out different tasks.<br/>
Using forecastguy one could find forecast of any place on any day at any time, meaning hourly, monthly and current day options.</h5>
<br>I have tried to cover most of the essential task, if required I will also cover the Optional tasks<br/>
<br>
<h2> Requirements:</h2>
(0) python 3+ <br/>
(1) requests <br/>
(2) urllib3  <br/>
(3) prettytable  <br/>
<br>

<h2>Installation:</h2>
1. Clone the repository or download and extract manually <br/>
2. cd to folder and execute `pip install -r requirements.txt` <br/>
3. test `python forecast.py -h`
<br/>
<h2>Usuage:</h2>
```
python forecast.py place [-t/--type hourly] [-d/--date day/month/year]
```
<br></br>place: can be any district, locality, city, keyword, etc <br/>
-t/--type: current(display current forecast)/hourly(display today's hourly forecast)/5days(5 days forecast)/15days(15 days forecast)/daily<br/>
-d/--date day/month/year (After 1/1/2014) <br/>
<h8>only one of -t or -d should be passed at a time</h8><b/r>
<h2> Examples: </h2>
  <p>python forecast.py mumbai</p>

python3 forecast.py "New kartarpur" -d 10/10/2019 

python3 forecast.py Bellandur -t hourly

