class BaseBlade():
	"""
	Blades define transformations ginsu will make to data.
	Ginsu can run them at two different points in the process
	either while the data is in a petl table (to make use of
	petl specific transformations) or while it is being streamed
	out as json (for more custom transformations)
	"""

	def __init__(self, stage):
		self.stage = stage
	
	def getStage(self):
		return self.stage

	def run(self, row):
		return row
