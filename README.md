# canTot

canTot is a python-based cli framework based on sploitkit and is easy to use because it similar to working with Metasploit. This similar to an exploit framework but focused on known CAN Bus vulnerabilities or fun CAN Bus hacks. It can also be used as a guide for pentesting vehicles and learning python for Car Hacking the easier way. This is not to reinvent the wheel of known CAN fuzzers, car exploration tools like caring caribou, or other great CAN analyzers out there. But to combine all the known vulnerabilities and fun CAN bus hacks in automotive security.

# Installation

```
git clone https://github.com/shipcod3/canTot
cd canTot
pip3 install -r requirements.txt
```
Note: Works better with Kali and Ubuntu

# Sample framework usage:

```
─$ python3 main.py 

                                                                                                                                                                                                                  
                                                                             @@@@@@@   @@@@@@   @@@  @@@  @@@@@@@   @@@@@@   @@@@@@@                                                                              
                                                                            @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@  @@@@@@@@  @@@@@@@                                                                              
                                                                            !@@       @@!  @@@  @@!@!@@@    @@!    @@!  @@@    @@!                                                                                
                                                                            !@!       !@!  @!@  !@!!@!@!    !@!    !@!  @!@    !@!                                                                                
                                                                            !@!       @!@!@!@!  @!@ !!@!    @!!    @!@  !@!    @!!                                                                                
                                                                            !!!       !!!@!!!!  !@!  !!!    !!!    !@!  !!!    !!!                                                                                
                                                                            :!!       !!:  !!!  !!:  !!!    !!:    !!:  !!!    !!:                                                                                
                                                                            :!:       :!:  !:!  :!:  !:!    :!:    :!:  !:!    :!:                                                                                
                                                                             ::: :::  ::   :::   ::   ::     ::    ::::: ::     ::                                                                                
                                                                             :: :: :   :   : :  ::    :      :      : :  :      :                                                                                 
                                                                                                                                                                                                                  
                                                                                                                                                                                                                  
                                                                                                         ███████████           █████                                                                              
                                                                                                        ░█░░░███░░░█          ░░███                                                                               
                                                                            ██████   ██████   ████████  ░   ░███  ░   ██████  ███████                                                                             
                                                                           ███░░███ ░░░░░███ ░░███░░███     ░███     ███░░███░░░███░                                                                              
                                                                          ░███ ░░░   ███████  ░███ ░███     ░███    ░███ ░███  ░███                                                                               
                                                                          ░███  ███ ███░░███  ░███ ░███     ░███    ░███ ░███  ░███ ███                                                                           
                                                                          ░░██████ ░░████████ ████ █████    █████   ░░██████   ░░█████                                                                            
                                                                           ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░    ░░░░░     ░░░░░░     ░░░░░                                                                             
                                                                                                                                                                                                                  
                                                                                                                                                                                                                  
                                                                                    >> quick and dirty canbus h4xing framework                                                                                    
                                                                                                   >> @shipcod3                                                                                                   
                                                                                                                                                                                                                  
                                                                                                                                                                                                                  
 

        -=[ 13 uncategorized ]=-                                                                                                                                                                                  
                                                                                                                                                                                                                  
cantot > show modules                                                                                                                                                                                             

Uncategorized modules
=====================

   Name                         Path  Enabled  Description                                                                                                                                                     
   ----                         ----  -------  -----------                                                                                                                                                     
   cherokee_kill_brakes         .     Y        This module will bleed all the brakes on the 2014 Jeep Cherokee while the car is moving. This has the result that the brakes will not work during this time and 
                                               has significant safety issues, even if it only works if you are driving slowly.                                                                                 
   cherokee_kill_engine         .     Y        This module will kill the engine on the 2014 Jeep Cherokee while the car is moving at low speed by killing a particular fuel injector.                          
   cherokee_turn_steering       .     Y        This module will put the Parking Assist Module(PAM) in diagnostic session and send a CAN message to tell the power steering ECU to turn the wheel for the Jeep  
                                               Cherokee 2014.                                                                                                                                                  
   diagnostic_state             .     Y        This module will keep the vehicle in a diagnostic state on loop by sending tester present packet.                                                               
   ecu_hard_reset               .     Y        This module performs hard reset in the ECU Reset Service Identifier (0x11).                                                                                     
   ford_escape_door_ajar_spoof  .     Y        This module will indicate that the door is ajar (open) from the instrument panel despite not opened.                                                            
   ford_escape_kill_engine      .     Y        This module will kill the engine for Ford Escape 2010 without establishing a diagnostic session and works at any speed.                                         
   jeep_wrangler_evicsend       .     Y        This module allows you to display the word Hacked on a 2012 Jeep Wrangler EVIC.                                                                                 
   kill_bus                     .     Y        This module will perform a known denial of service via the CAN bus called Firehose attack.                                                                      
   malibu_overheat              .     Y        This module will flood temp gauge on a 2006 Malibu.                                                                                                             
   mazda_ic_mover               .     Y        This module moves the needle of the accelorometer and speedometer of the Mazda 2 instrument cluster.                                                            
   prius_park_kill_engine       .     Y        This module will kill the fuel to individual or all cylinders in the internal combustion engine of a Toyota Prius 2010 but requires it to be parked.            
   reset_mileage                .     Y        This module clears diagnostic trouble codes and resets the mileage.

cantot > use diagnostic_state                                                                                                                                                                                     
cantot (diagnostic_state) > show options                                                                                                                                                                          

Module options
==============

   Name       Value  Required  Description                     
   ----       -----  --------  -----------                     
   ARBID      2015   Y         Arbitration ID (Default: 0x7DF) 
   INTERFACE  vcan0  Y         CAN interface                   

cantot (diagnostic_state) > run                                                                                                                                                                                   
[*] Putting the vehicle in a diagnostic state...
Press Ctrl+C to stop or cancel
```

## Author
Jay Turla

## Contributors
- To be updated

## Credits
- Nikhil Bogam for CVE-2022-26269 and allowing me to port his findings.
- Charlie Miller and Chris Valasek for their [research](https://illmatics.com/carhacking.html) and papers.
- Ian Tabor (mintynet) for his advises and mentorship.
- Car Hacking Village
- Eric Evenchick for pyvit
- Alexandre D'Hondt for sploitkit
- carfucar for canfuzz_sids.py inspiration
- Craig Smith for the Car Hacker's Handbook and hwbridge inspiration
