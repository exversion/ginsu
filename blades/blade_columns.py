from src.blades import BaseBlade
import petl

class ColumnsBlade(BaseBlade):
	def __init__(self):
		BaseBlade.__init__(self, 'pre')

	def run(self, table, meta):
		#Fix missing columns

		#Convert spaces to underscores
		petl.transform.headers.rename(table, r'\s', '_')

		#
		return table