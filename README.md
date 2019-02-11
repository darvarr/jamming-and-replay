# jamming-and-replay
A jamming-and-replay attack against RKES using SDR

Modern Remote Keyless Entry Systems (RKESs) employes Rolling Code to avoid replay-attack. This mechanism makes signals to be usable only once. The attack is intended to be used to obtain a valid opening signal for the car. It is important to point that this attack is feasible against EVERY RKES, like cars, gates, garages door etc.. The attack is done as follows:

1. Jamming the first communication between the car and the remote, in the meanwhile recording the valid signal;
2. A normal user is convinced that the car's didn't "hear" the remote's signal and repeat the latter operation;
3. Jamming the second communication, recording the valid signal and replay the first recorded signal

After the previous steps, an attacker is able to obtain a valid opening signal which the car never heard before. How to use it is up to the attacker. In my case, I imagine to follow the victim and jam the closing signal after he parks the car. By doing so, he is forced to use the physical backup key to close it, make it easier to brake into the car. 

For the hardware part, I employed a Ettus USRP B210 Software Defined Radio (SDR) and a laptop. For the software part, I used GNURadio, an open source library for programming SDRs. It comes with a graphical environment which converts the "block" design into python scripts. In order to perform the attack it is needed to set the paramenters of 1) frequency of operation of the car's remote 2) cut-off of the low-pass filter 3) gain for both receiver and transmitter 4) device address for your USRP. This can be done directly in the python files or in the flowgraph.
