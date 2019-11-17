# lists IDs of running ec2 instances

import json
import subprocess

PAYLOAD = ['aws', 'ec2', 'describe-instances']

out = subprocess.Popen(PAYLOAD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
data = json.loads(stdout)

for res in data['Reservations']:
    # cycle through reserved instances and check to see if in running state
    for instance in res['Instances']:
        if (instance['State'])['Name'] == 'running':
            print(instance['InstanceId'])
