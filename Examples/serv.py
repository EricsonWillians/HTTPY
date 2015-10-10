from Amazonia.main import WebPage, WebApp

webpage = WebPage()

webpage.link_css("css/bootstrap.min.css", "font-awesome/css/font-awesome.min.css")
webpage.add_meta_tags(
	charset=("utf-8",), 
	name=("viewport", "width=device-width, initial-scale=1"),
	author=("Ericson Willians",))

application = WebApp(webpage)
