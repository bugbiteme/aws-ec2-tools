for i in `python get-ec2-running-instances.py`
  do
    aws ec2 terminate-instances --instance-ids $i
  done
