from tribus import BASEDIR
from tribus.common.utils import get_path
from tribus.common.recipes.recipe import RecipeDir


test_path = get_path([BASEDIR, 'tribus', 'data', 'services', 'wiki'])


rd = RecipeDir(test_path)

print rd.metadata.name

print rd.metadata.description
print rd.metadata.components
print type(rd.metadata.components)

# print rd.name
# print rd.summary
# print rd.maintainer
# print rd.description

