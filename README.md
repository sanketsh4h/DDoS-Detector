# DDoS Detector

## 1. Description

DDoS Detector, as the name suggests aims at detecting and alerting its user of DDoS attacks before the attack may do any plausible damage (In case you don't know what a DDoS attack is, you may refer to section 2 of this text). This project is programmed in python and is divided in two modules:

### 1.1. Packet Sniffing:
 This Project captures and detects packets in real time. To capture the packets in real-time, this project uses Scapy library. (Information on how to install Scapy is provided in Section 3 of this text.)

### 1.2 Classification:
To classify the captured packets, a Multi-Layer Perceptron classifier is used. To implement the same, scikit-learn library has been used. (Information on how to install scikit-learn is provided in Section 3 of this text.) To train the classifier, the Revised KDD Cup Dataset is being used. 

## 2. What is a DDoS Attack?

Distributed Denial of Service (DDoS) attack is a type of attack that takes advantage of the specific capacity limits that apply to any network resources – such as the infrastructure that enables a company’s website. The DDoS attack will send multiple requests to the attacked web resource – with the aim of exceeding the website’s capacity to handle multiple requests… and prevent the website from functioning correctly


##  3. Requirements

### 3.1. Necessary Dependencies
To run the code, the user needs to have installed the following libraries:
- Scapy
- scikit-learn
- pickle

You may install these by entering the following commands in the terminal (It is assumed that you have 'pip' installed)
```bash
pip install scapy
pip install sklearn
pip install pickel
```
### 3.2 Additional Dependencies
The user may install the following dependencies if they wish to modify the Jupyter Notebook provided in this repository. Any regular user doesn't need to install these dependencies:
- numpy
- pandas

You may install these by entering the following commands in the terminal (It is assumed that you have 'pip' installed)
```bash
pip install numpy
pip install pandas
```
## 4. Usage

The user may clone the whole repository on their device and run the 'run.py' file in their python terminal. 

The script shall run in the background while the user may do anything else on their device. The program will alert the user by printing a specific message on the terminal. The message will contain the IP address of the said attacker and the user may take whatever measures to deal with them.

## 5. How to Test
To test the program, the user may perform a DDoS attack themselves. 
To perform a DDoS attack, type in the following command in the terminal:
```bash
ping -t <insert url or IP address>
```

This will make the program print a message on the terminal that contains the IP address of the attacker and the victim as explained before.


## 6. License
[MIT](https://choosealicense.com/licenses/mit/)
