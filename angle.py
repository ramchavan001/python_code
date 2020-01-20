
# Python program to find angle between hour and minute hands 


def calcAngle(h,m): 
		
		
		if (h < 0 or m < 0 or h > 12 or m > 60): 
			print('Invalid input') 
		
		if (h == 12): 
			h = 0
		if (m == 60): 
			m = 0
		
	
		hour_angle = 0.5 * (h * 60 + m) 
		minute_angle = 6 * m 
		
		#difference between two angles 
		
		angle = abs(hour_angle - minute_angle) 
		
		# Return the smaller angle of two 
		# possible angles 
		angle = min(360 - angle, angle) 
		
		return angle 
		
h = int(input("enter the hour: "))
m = int(input("enter the minut: "))
print('Angle ', calcAngle(h,m)) 


