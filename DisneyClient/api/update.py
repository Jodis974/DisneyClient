



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



from aiohttp import web

import infrastructure

class Update(web.View):
	async def get(self):
		return web.json_response({
			"client_version": infrastructure.config.get("client_version"),
			"standalone_url": infrastructure.config.get("standalone_url"),
			"update_url": infrastructure.config.get("update_url"),
			"version": infrastructure.config.get("version")})



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



