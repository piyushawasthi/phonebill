#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Call:
	def __init__(self, duration):
		hours, minutes, seconds = tuple(duration.split(":"))
		self.hours = int(hours)
		self.minutes = int(minutes)
		self.seconds = int(seconds)

	def duration_in_seconds(self):
		return self.hours * 3600 + self.minutes * 60 + self.seconds

	def cost(self):
		duration = self.duration_in_seconds()
		if duration < 300:
			return duration * 3
		else:
			extra_minute = self.seconds > 0 and 1 or 0
			return (self.hours * 60 + self.minutes + extra_minute) * 150