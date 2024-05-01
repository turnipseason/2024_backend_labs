from cache import LRUCache

cache = LRUCache(-10) # сообщение об ошибке по причине неправильного размера кэша 
cache = LRUCache(3)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')

print(cache.get('Jesse')) # вернёт 'James'

cache.rem('Walter')

print(cache.get('Walter')) # вернёт ''

cache.rem('Banana') # такого у нас не было, возвращаем сообщение об ошибке

cache.set('Nana', 'Lalala')
cache.set('Lala', 'Nanana')
cache.set('Moon', 'Sun')  # сообщение о слишком большом количестве элементов