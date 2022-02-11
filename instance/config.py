class Config(object):
	DEBUG = False
	TESTING = False

class Development(Config):
	DEBUG = True

class Production(Config):
	DEBUG = False

class Testing(Config):
	TESTING = True
		

app_config = {
	'development':Development,
	'Testing':Testing
}