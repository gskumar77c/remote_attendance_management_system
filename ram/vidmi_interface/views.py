from django.shortcuts import render
from vidmi_interface.models import address
from background_task import background
from attendance.models import api_queue
# Create your views here.
def send_data(path):
        ipaddr,port,token=address.connection_info()
        '''
        here we implement sending data over that connection
        once we get the protocol and interfacing for it this would be completed
        '''

@background
def check_pending():
    print("Checking pending files")
    entries=api_queue.objects.filter(status="pending")
    for entry in entries:
        #result=send_data(entry)
        print(entry)
        '''
        send and recieve entry and store appropriately in database
        '''
    return




