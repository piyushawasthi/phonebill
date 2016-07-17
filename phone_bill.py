#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.number_bill import NumberBill

def get_number_bill(telephone, bill):
	if not telephone in bill:
		bill[telephone] = NumberBill(telephone)
	return bill[telephone]

def solution(log):
	bill = {}
	for line in log.split("\n"):
		duration, telephone = tuple(line.split(","))
		number_bill = get_number_bill(telephone, bill)
		number_bill.add_call(duration)

	paid_bills = sorted(bill.values(), cmp=NumberBill.cmp_by_duration)[1:]
	paid_bills_costs = [ number_bill.cost() for number_bill in paid_bills ]
	return reduce(lambda a, b: a + b, paid_bills_costs, 0)


def test():
	log = "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"
	assert solution(log) == 900

if __name__ == "__main__":
	test()