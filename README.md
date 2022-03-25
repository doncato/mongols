# mongols
A simple, small script to quickly show all the contents of a mongo db
## Installation
1. You need to have `python3` installed.
2. Clone this repository `git clone https://github.com/doncato/mongols`
3. Change the workdirectory to the cloned repository `cd mongols/`
4. Install the requirements `pip3 install -r requirements.txt`
## Usage
As a standalone script:<br>
`python3 main.py mongodb://example.com:27017/`

From another script:<br>
`from main import list_all`
`content = list_all("mongodb://example.com:27017/")`

