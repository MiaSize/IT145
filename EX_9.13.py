
from typing import OrderedDict


favorite_languages = OrderedDict()

favorite_languages['parent'] = 'is used to describe the base code'
favorite_languages['child'] = "is the child code of the parent meaning it is the same code as the parent but can have alters to it"
favorite_languages['class'] = "is used to define a class for a block of code"
favorite_languages['import'] = "is used to import code in the same folder to another file"
favorite_languages['from'] = "is used to determine which file the import will grab from"

for name, define in favorite_languages.items():
    print(name.title(), define + '.')
