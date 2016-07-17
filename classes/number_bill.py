#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.call import Call

class NumberBill:
	def __init__(self, telephone):
		self.telephone = telephone
		self.calls = []

	def add_call(self, duration):
		self.calls.append(Call(duration))

	def total_duration(self):
		individual_durations = [ call.duration_in_seconds() for call in self.calls ]
		return reduce(lambda a, b: a + b, individual_durations, 0)

	def cost(self):
		individual_costs = [ call.cost() for call in self.calls ]
		return reduce(lambda a, b: a + b, individual_costs, 0)

	@staticmethod #decreasing order
	def cmp_by_duration(number_bill, another_number_bill):
		if number_bill.total_duration() < another_number_bill.total_duration():
			return 1
		elif number_bill.total_duration() == another_number_bill.total_duration() and another_number_bill.telephone < number_bill.telephone:
			return 1
		else: return -1