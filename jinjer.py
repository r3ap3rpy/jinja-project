from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('templates')

env = Environment(loader = loader)

template = env.get_template('Campaign.tpl')

result =  template.render({'Title':'Make the world a better place!','Message':'Every individual should work on that separately!','Mission':'Make Doom Eternal the most epic game possible!'})

with open('index.html','w') as index:
	index.write(result)