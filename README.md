# NIDS-TEST
Purpose: Send Three Test cases at different alert levels to test NIDS systems. This will send three packets that correspond with the IDS rules, that should help test placement and alerting of an IDS system. This utlizes safe traffic that doens't envolve using an actual exploit or scanning to test the IDS placement to make sure you are seeing all the traffic you intended to see. THis can be change to send over TCP however a reciving box needs to be sent up. UDP was chosen for ease of use, and so the IDS didn't have to track the state of the TCP conenction for these rules. 
