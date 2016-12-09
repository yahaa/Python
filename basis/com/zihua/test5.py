import datetime
time=raw_input('Enter a date (mm/dd/yyyy):')
moth=['January','February','March','April','May','June','July','August','Septemper','October','November','December']
t=time.split('/')
print ' The converted date is: '+moth[int(t[0])-1]+' '+t[1]+', '+t[2]
