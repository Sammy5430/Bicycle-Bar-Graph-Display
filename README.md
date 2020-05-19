**Bicycle Bar Graph Display**

Download and extract the zip file found in:
https://github.com/Sammy5430/Bicycle-Bar-Graph-Display

Open the terminal and navigate to the directory where the zip file was extracted.

Run the dataPlotter.py python file.

	When ran, you will see a loading window. This window will be displayed until connection is established with the Wi-Fi module.
	*Note: When the system is on, the Wi-Fi module creates a Wi-Fi access point to which the computer must be connected, in order to receive the data. Password for the connection is msp430.*

	Once connection is established, the software will start automatically. 
	
	A new window will be created, containing a bar plot that will be updated every second (occasionally works slower on windowsOS) to show the measurements from the system.
	*Note: real-time plotting was not possible due to limitations in the system.*

	This will go on for as long as the system is on, logging the elapsed time and adjusting the scale of each plot if necessary.

	Once the system turns off, the window with the bar plot will close and a new window will open, showing the summary of the run.

	Here you will see the final elapsed time, max values obtained for each measurement and some additional information requested by the client.

	If you press the restart button, the software will reset and will go back to the loading window.

Logs for all runs can be found on resources/files/logfile.csv