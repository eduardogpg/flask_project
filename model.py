#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import peewee

DATABASE = peewee.MySQLDatabase("flask_course", host="localhost", port=3306, user="root", password = "")

class Comment(peewee.Model):
	username = peewee.CharField(max_length=50)
	email = peewee.CharField(max_length=50)
	text = peewee.TextField(default='')
	created_date = peewee.DateTimeField(default=datetime.datetime.now)
  
	class Meta:
		database = DATABASE
		db_table = "comments"

	def get_date(self):
		value = self.created_date
		months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
		month = months[value.month]
		return "{} de {} del {}".format(value.day, month, value.year )
	
if __name__ == '__main__':
	if not Comment.table_exists():
		Comment.create_table()