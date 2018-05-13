# Author: Ryan McCormick
# Purpose: Code written to simulate graphs from 
#		   NumberPhile video on the golden ratio: 
#		       https://www.youtube.com/watch?v=sj8Sg8qnjOg

import sys # to exit gracefully
import math # opted for built-in over numpy to avoid users needing to install
import matplotlib.pyplot as plt

def plot_flower():
	# Fraction of full rotation to turn before plotting next point
	try:
		turn_fraction = float(input("Enter fraction of full turn (Golden Ratio by default): "))
		# Convert numbers over 1 to be between 0 and 1. ex) 1.5 -> 0.5
		turn_fraction -= int(turn_fraction)
	# Catch Ctrl+C
	except KeyboardInterrupt:
		sys.exit()
	# Catch bad inputs
	except:
		# Golden ratio by default
		turn_fraction = (math.sqrt(5) - 1.0) / 2

	try:
		NUM_POINTS = int(input("Enter number of points to plot (100 by default): "))
	# Catch Ctrl+C
	except KeyboardInterrupt:
		sys.exit()
	# Catch bad inputs
	except:
		NUM_POINTS = 100


	# Set theta to 0 initially
	theta = 0
	# Initial distance of 1 from origin 
	distance = 1
	# Initial (x,y) coords at distance = 1 and theta = 0
	x_points = [distance*math.cos(math.radians(theta))]
	y_points = [distance*math.sin(math.radians(theta))]

	# Get figure on screen to view continuous updates
	plt.show()

	# Dynamic limits on graph to fit points nicely regardless of parameters
	bound = NUM_POINTS * (turn_fraction)
	# Catch 0 to fix bounds of figure
	if bound == 0:
		bound = NUM_POINTS

	# Get the current figure being shown
	axes = plt.gca()
	# Set limits of figure based on dynamic bound
	axes.set_xlim(-bound, bound)
	axes.set_ylim(-bound, bound)

	# Plot initial coordinates
	axes.scatter(x_points, y_points)

	# Plot the rest of the points while rotating around origin
	for i in range(NUM_POINTS):
		# Update theta by user-defined turn_fraction
		theta = (theta + (turn_fraction*360))
		# If we've completed a full loop around origin or turn_fraction is 0...
		if theta >= 360 or theta == 0:
			# Keep theta within [0, 360]
			theta = theta % 360
			#increase distance to avoid overlapping points
			distance += 1

		# Add next point after rotating
		x_points.append(distance*math.cos(math.radians(theta)))
		y_points.append(distance*math.sin(math.radians(theta)))

		# Dynamically update plot
		# this might not be the best way to do it, but it got the job done. 
		# Seems easier to have dynamic line plot but scatter plot was finnicky
		axes.clear()
		axes.set_xlim(-bound, bound)
		axes.set_ylim(-bound, bound)

		# Dynamically size plotted points based
		if NUM_POINTS < 100:
			# Default point size is 20
			axes.scatter(x_points, y_points)
		else:
			# Reduce point size if plotting many points for clean plot
			axes.scatter(x_points, y_points, s=4000/(NUM_POINTS))

		# Introduce slight pause to see graph updating as it goes
		plt.pause(1e-19)

	# Keep the plot on the screen after loop finishes
	plt.show()

if __name__ == '__main__':
	try:
		plot_flower()
	# Catch Keyboard-Interrupt (Ctrl+C)
	except:
		print('\nExiting...')

