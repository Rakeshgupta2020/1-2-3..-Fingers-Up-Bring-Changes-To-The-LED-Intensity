# 1-2-3..-Fingers-Up-Bring-Changes-To-The-LED-Intensity

This project is to control the LED light intensity using the number of fingers (1/2//3/4..) using opencv, cvzone and BoltIoT 
i.e based on the number of figures we show during video capture by the system it will make changes the light intensity of the LED 
using the bolt API enables the smart control of LED's intensity using computer vision


Steps to follow:
1.  setup the hardware connections according to the circuit diagram and process mentioned below
Connect one end of 330 ohms resistor to the anode of LED and another end of the resistor to pin 0 of the Bolt WiFi module using jumper wires and connect the cathode of the LED to the GND pin of bolt module using a jumper wire
![cover_git](https://github.com/Rakeshgupta2020/1-2-3..-Fingers-Up-Bring-Changes-To-The-LED-Intensity/assets/126176140/d6af3263-ffab-452e-9234-72e58f8cd898)

3. Keep the Bolt cloud API and device id in another python file and name them as conf
4. Import the necessary libraries like opencv, cvzone, boltiot and conf make sure to install the libraries like opencv, cvzone and boltiot before importing them (pip install opencv, pip install cvzone and pip install boltiot)
5. Download the code and do run and observe the results

![results_pic](https://github.com/Rakeshgupta2020/1-2-3..-Fingers-Up-Bring-Changes-To-The-LED-Intensity/assets/126176140/358857c8-44db-463e-958f-b4e0c2b04721)
