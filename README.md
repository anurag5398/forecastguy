# forecastguy
<h5>
Forecastguy is a CLI for finding forecast of any place on any day at any time, meaning hourly, monthly and current day.</h5>

<br></h5>
<h2> Requirements:</h2>
(0) python 3+ <br/>
(1) requests <br/>
(2) urllib3  <br/>
(3) Flask
(4) prettytable  <br/>
<br>

<h2>Installation:</h2>
1. Clone the repository or download and extract manually <br/>
2. cd to folder and execute <i>pip install -r requirements.txt</i> <br/>
3. test <i>python forecast.py -h</i>
<br/>
<h2>Usage:</h2>

> python forecast.py place [-t/--type hourly] [-d/--date day/month/year]
<br></br>
> place: can be any district, locality, city, keyword, etc <br/>
> -t/--type: current(display current forecast)/hourly(display today's hourly forecast)/5days(5 days forecast)/15days(15 days forecast)/daily<br/>
> -d/--date day/month/year (After 1/1/2014) <br/>
<h7><br>only one of -t or -d should be passed at a time</h7><br/>
<h2> Examples: </h2>
  <p>python forecast.py mumbai</p>

python3 forecast.py "New kartarpur" -d 10/10/2019 

python3 forecast.py Bellandur -t hourly

