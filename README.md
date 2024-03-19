<h1>Simple CRUD operations with Python and Postgre Database</h1>

<h2>Run Instructions:</h2>

<p>This program relies on the user having a Postgre database.</p>
To run:
<ol>
    <li>To install the required dependcies, enter the follwoing in the terminal: pip install -r requirements.txt</li>
    <i>I would reccommend setting up a python virtual environment to set up these dependencies</i>
    <li> Edit the paramets in the <i>psycop.connect()</i> function on line 6 in the file <i>"connect.py"</i> The following information needs to be correct, or the program will not run: host - Hostname of device, dbname - Name of database, user - Username of user, password - Password assocaited with that user</li>
    <li>The program will automatically check for the existance of a students table and fill it with default data if no data exists.</li>
    <li> In terminal, enter the following: python3 main.py </li>
    <i> Note: use whatever python command works for your system</i>
</ol>

<h2>While using:</h2>
<p> This is a command line interface application. The user will be prompted with a menu of options. Depending on what is selected, the user will be
prompted with entering additional information.</p>
Options:
<ol>
<li>Preview Users</li>
<li>Add user</li>
<li>Edit user</li>
<li>Delete user</li>
<li>Exit</li>
</ol>
    