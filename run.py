from scapy.all import *
import pickle as pkl
import sklearn

icmp_model = pkl.load(open("icmp_model.pkl", 'rb')) # Loading the trained ML model (KNN)

def sniffp(pkt): # a garbage function to pass to scapy.sniff function
    return

def predicting(features,model):
    prediction = model.predict(features) #Function for real time classification of packets
    return prediction


def main():

    while True:
        packet = sniff(prn=sniffp, filter='icmp', count=1) #capturing one packet
        size = int(len(packet[0])) #size of the packet as packet feature
        serv = getattr(packet[0][ICMP], "type") #getting the type of service (echo request (8) or reply (0))
        if serv == 8:       # changing values of services according to ML model
            serv = 0.0
        elif serv == 0:
            serv = -0.1

        seqnum = getattr(packet[0][ICMP], "seq") # getting sequence number as a packet feature
        features = [(serv, size, seqnum)] # getting features ready to feed them to model
        prediction = predicting(features,icmp_model) #classifying the packet, 1 for malicious and 0 for normal
        if prediction == 1:
            srcIP = getattr(packet[0][IP], "src") #getting source IP of the captured packet
            dstIP = getattr(packet[0][IP],"dst") # getting destination IP of the captured packet
            if serv == 0.0:
                print(str(dstIP) + " is being attacked by " + str(srcIP)) #printing statement if attack detected
            elif serv == -0.1:
                print(str(srcIP) + " is being attacked by " + str(dstIP))


main()