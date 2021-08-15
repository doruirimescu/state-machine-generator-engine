import unittest
from blueprint import Blueprint

#   Label                               Left                        Right                    Up                 Down                                Select
a = (("Menu_1",                         "Menu_2",                   -1,                     -1,                 "Menu_1_Feature_1",                 "Enter_game_1"),
     ("Menu_2",                         "Menu_3",                   -
      1,                     -1,                 "Menu_2_Feature_1",                 -1),
     ("Menu_3",                         -1,                         -
      1,                     -1,                 "Menu_3_Feature_1",                 -1),
     ("Menu_1_Feature_1",               "Menu_1_Feature_2",         -
      1,                     -1,                 "Menu_1_Feature_1_Subfeature_1",    -1),
     ("Menu_1_Feature_2",               -1,                         -
      1,                     -1,                 -1,                                 -1),
     ("Menu_1_Feature_1_Subfeature_1",  -1,                         -
      1,                     -1,                 -1,                                 -1),
     ("Menu_3_Feature_1",               -1,                         -
      1,                     -1,                 -1,                                 -1),
     ("Menu_2_Feature_1",               -1,                         -
      1,                     -1,                 -1,                                 -1),
     ("Enter_game_1",                   -1,                         -
      1,                     -1,                 -1,                                 -1)
     )


outputs = ("std::cout<<\"1\"<<std::endl;",
           "std::cout<<\"2\"<<std::endl;",
           "std::cout<<\"3\"<<std::endl;",
           "std::cout<<\"4\"<<std::endl;",
           "std::cout<<\"5\"<<std::endl;",
           "std::cout<<\"6\"<<std::endl;",
           "std::cout<<\"7\"<<std::endl;",
           "std::cout<<\"8\"<<std::endl;",
           "std::cout<<\"Game1\"<<std::endl;")

actionList = ("Left",  "Right", "Up",   "Down", "Select")



class TestBlueprint(unittest.TestCase):
    def test_stateOutputs(self):
        blueprint = Blueprint(a, outputs, actionList)
        self.assertEqual(blueprint.stateOutputs, outputs)

    def test_stateTransitionTable(self):
        blueprint = Blueprint(a, outputs, actionList)
        self.assertEqual(blueprint.stateTransitionTable, a)

    def test_actions(self):
        blueprint = Blueprint(a, outputs, actionList)
        self.assertEqual(blueprint.actions, actionList)

    def test_stateListLabels(self):
        blueprint = Blueprint(a, outputs, actionList)
        self.assertEqual(len(blueprint.stateList), 9)
        self.assertEqual(blueprint.stateList[0].label, "Menu_1")
        self.assertEqual(blueprint.stateList[4].label, "Menu_1_Feature_2")
        self.assertEqual(blueprint.stateList[8].label, "Enter_game_1")

    def test_stateListOutput(self):
        blueprint = Blueprint(a, outputs, actionList)
        for i in range(len(outputs)):
            self.assertEqual(blueprint.stateList[i].output, outputs[i])

    def test_stateListOutput(self):
        blueprint = Blueprint(a, outputs, actionList)
        self.assertEqual(blueprint.stateList[0].successors, {'Left': 1, 'Down': 3, 'Select': 8})
        self.assertEqual(blueprint.stateList[1].successors, {'Left': 2, 'Down': 7})
        self.assertEqual(blueprint.stateList[2].successors, {'Down': 6})
        self.assertEqual(blueprint.stateList[3].successors, {'Left': 4, 'Down': 5})
        self.assertEqual(blueprint.stateList[4].successors, {})
        self.assertEqual(blueprint.stateList[5].successors, {})
        self.assertEqual(blueprint.stateList[6].successors, {})
        self.assertEqual(blueprint.stateList[7].successors, {})
        self.assertEqual(blueprint.stateList[8].successors, {})

    def test_stateLabels(self):
        blueprint = Blueprint(a, outputs, actionList)
        print(blueprint.stateLabels)
        self.assertEqual(blueprint.stateLabels, ["Menu_1", "Menu_2", "Menu_3", "Menu_1_Feature_1", "Menu_1_Feature_2",
                         "Menu_1_Feature_1_Subfeature_1", "Menu_3_Feature_1", "Menu_2_Feature_1", "Enter_game_1"])
