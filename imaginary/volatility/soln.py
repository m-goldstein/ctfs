import os
filename =  '183D'
target = 'vol.vmem'
os.system('7z e {}'.format(filename))
os.system('strings {} | grep ictf'.format(target))
