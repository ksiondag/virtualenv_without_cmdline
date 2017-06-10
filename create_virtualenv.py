import os

import virtualenv

name = 'default'


path = os.path.join(os.path.dirname(__file__), name)

print('Creating environment "%s"' % name)
virtualenv.create_environment(name)
print('"%s" created' % name)
