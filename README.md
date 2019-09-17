# forecastguy
Forecastguy is CLI developed for demostration. It is not production ready or fully optimized. Time was a factor while developing this tool. Hope to make it better, in comming days. Code complies with pep8 standards. In future a separate JSON API will be developed for carrying out different tasks.
<br>
<h2> Requirements</h2>
(1) requests <br>
(2) urllib3  <br>
(3) prettytable  <br>
<br>

<h2>Installation</h2>

"git clone https://github.com/anurag5398/forecastguy.git"
<b>cd to Downloaded project/folder</b>
"pip install -r requirements.txt"

<h2> Usuage </h2><br>
python forecast.py place [-t current/hourly/5/15] [-d day(01-31)/month(01-12)/year]<br>
Only one parameter from -t/--type or -d/--date can be given as argument.<br>
Use 01,05 to Indicate Dates less than 10. (double digits)


