# GVE DevNet VRF SVI Validator
This repository contains the Python code for a script that will connect to switches, parse the 'show ip interface' and 'show vlan' commands, and then write the device name, interface, VRF, IP address, and VLAN of the Mgmt-vrf of each switch to an Excel sheet.

![/IMAGES/workflow.png](/IMAGES/workflow.png)

## Contacts
* Danielle Stacy

## Solution Components
* Catalyst
* Python 3.11
* pyATS
* Genie
* Excel

## Installation/Configuration
1. Clone this repository with `git clone https://github.com/gve-sw/gve_devnet_vrf_svi_validator.git`
2. Modify the testbed1.yml file with the information relevant to the switches you would like to pull the VRF and SVI information from. Replace the variables in braces with the appropriate values. For more information about how to structure the YAML file, find documentation [here](https://developer.cisco.com/docs/pyats/#!connection-to-devices/device-connections). 
3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
4. Install the requirements with `pip3 install -r requirements.txt`

## Usage
To run the code, use the command:
```
$ python3 check_vrf.py
```

After the code is complete, it will have created an Excel document called interface_details.xlsx
![/IMAGES/excel_output.png](/IMAGES/excel_output.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.