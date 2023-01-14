import unittest
from blueprint import Blueprint, initialize_blueprint

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
        blueprint = initialize_blueprint(a, outputs, actionList)
        self.assertEqual(blueprint.state_outputs, outputs)


    def test_actions(self):
        blueprint = initialize_blueprint(a, outputs, actionList)
        self.assertEqual(blueprint.actions, actionList)

    def test_stateListLabels(self):
        blueprint = initialize_blueprint(a, outputs, actionList)
        self.assertEqual(len(blueprint.state_list), 9)
        self.assertEqual(blueprint.state_list[0].label, "Menu_1")
        self.assertEqual(blueprint.state_list[4].label, "Menu_1_Feature_2")
        self.assertEqual(blueprint.state_list[8].label, "Enter_game_1")

    def test_stateListOutput(self):
        blueprint = initialize_blueprint(a, outputs, actionList)
        for i in range(len(outputs)):
            self.assertEqual(blueprint.state_list[i].output, outputs[i])

    def test_stateListOutput(self):
        blueprint = initialize_blueprint(a, outputs, actionList)
        self.assertEqual(blueprint.state_list[0].successors, {'Left': 1, 'Down': 3, 'Select': 8})
        self.assertEqual(blueprint.state_list[1].successors, {'Left': 2, 'Down': 7})
        self.assertEqual(blueprint.state_list[2].successors, {'Down': 6})
        self.assertEqual(blueprint.state_list[3].successors, {'Left': 4, 'Down': 5})
        self.assertEqual(blueprint.state_list[4].successors, {})
        self.assertEqual(blueprint.state_list[5].successors, {})
        self.assertEqual(blueprint.state_list[6].successors, {})
        self.assertEqual(blueprint.state_list[7].successors, {})
        self.assertEqual(blueprint.state_list[8].successors, {})

    def test_stateLabels(self):
        blueprint = initialize_blueprint(a, outputs, actionList)
        print(blueprint.state_labels)
        self.assertEqual(blueprint.state_labels, ["Menu_1", "Menu_2", "Menu_3", "Menu_1_Feature_1", "Menu_1_Feature_2",
                         "Menu_1_Feature_1_Subfeature_1", "Menu_3_Feature_1", "Menu_2_Feature_1", "Enter_game_1"])
