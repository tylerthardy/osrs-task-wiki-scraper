import api

import items
import npcs
import combat_tasks
import league1_tasks
import league2_tasks

api.use_cache = True

items.run()
npcs.run()
combat_tasks.run()
league1_tasks.run()
league2_tasks.run()
