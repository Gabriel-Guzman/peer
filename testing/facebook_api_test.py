from urllib.request import urlopen

def main():
	#to find go to page's FB page, at the end of URL find username
	#e.g. http://facebook.com/walmart, walmart is the username
	graph_url = "https://graph.facebook.com/"

	APP_ID = 165008204006667
	APP_SECRET = 0f725ad8b39da0a2f612b1620c2f11c7

	post_url = create_post_url(graph_url, APP_ID, APP_SECRET)

	web_response = urlopen(post_url)
	

def create_post_url(graph_url, APP_ID, APP_SECRET):
	#method to return 
	post_args = "/posts/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
	post_url = graph_url + post_args

	return post_url
