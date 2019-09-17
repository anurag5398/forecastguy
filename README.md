# forecastguy
Forecastguy is CLI developed for demostration. It is not production ready or fully optimized. Time was a factor while developing this tool. Hope to make it better, in coming days. Code complies with pep8 standards. In future a separate JSON API will be developed for carrying out different tasks.<br>
Using forecastguy one could find forecast of any place on any day at any time, meaning hourly, monthly and current day options.
<br>
<h2> Requirements</h2>
(1) requests <br>
(2) urllib3  <br>
(3) prettytable  <br>
python3 is also required<br>
<br>

<h2>Installation</h2>

<b>"git clone https://github.com/anurag5398/forecastguy.git" or Navigate to "https://github.com/anurag5398/forecastguy" and Download zip. </b><br>
<b>cd to Downloaded project/folder</b><br>
<b>"pip install -r requirements.txt"<br></b>

<h2>Usuage </h2><br>
python forecast.py place [-t current/hourly/5/15] [-d day(01-31)/month(01-12)/year]<br>
Only one parameter from -t/--type or -d/--date can be given as argument.<br>
Use 01,05 to Indicate Dates less than 10. (double digits)

<br>
place : It could be any district, city, town ,... <br>
-t/--type : This is optional, default is current. (Ex. --type daily/monthly/15days) <br>
-d/--date : This is also optional, default is today (Ex. --date 02/04/2019) <br>

<h2> Examples </h2>
./forecast.py Mumbai -t now <br>
python3 forecast.py kartarpur -d 10/10/2019 <br>
python3 forecast.py Bellandur<br>
