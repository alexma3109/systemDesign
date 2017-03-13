class userService:
	def getUser(self, user_id):
		key = "user::%s" % user_id
		user = cache.get(key)
		if user:
			return user
		user = database.get(user_id)
		cache.set(key, user)
		return user

	def setUser(self, user):
		key = "user::%s" % user.id
		cache.delete(key); # if both set, and cache success and database failed, it will be inconsistence #
		database.set(user);