#!/usr/bin/python2
import trivia
import unittest
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class DetailsOfGameTest(unittest.TestCase):
    
    def test_the_players_counter(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        self.assertEqual(game.how_many_players, 2)
        logging.info("Check, that numbers of players is counted good or not\n")

    def test_game_is_not_playable(self):
        game = trivia.Game()
        self.assertFalse(game.is_playable())
        logging.info("\nThe game is not playable without any player\n")
        
    def test_game_is_not_playable_with_one_player(self):
        game = trivia.Game()
        game.add('Susan')
        self.assertFalse(game.is_playable())
        logging.info("The game is not playable with one player\n")

    def test_game_is_playable_with_two_players(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        self.assertTrue(game.is_playable())
        logging.info("The game is playable with two players\n")

    def test_game_is_playable_with_more_players(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        game.add('Susan')
        game.add('Carl')
        self.assertTrue(game.is_playable())
        logging.info("The game is playable with more players\n")

    
    def test_current_category_is_rock(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        game.places[0] = 3
        actual_result_of_current_category = game._current_category
        self.assertEqual(actual_result_of_current_category, 'Rock')
        logging.info("The current category is: " + actual_result_of_current_category +"\n")

    def test_current_category_is_science(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        game.places[game.current_player] = 5
        actual_result_of_current_category = game._current_category
        self.assertEqual(actual_result_of_current_category, "Science")
        logging.info("The current category is: " + actual_result_of_current_category + " for " + game.players[game.current_player]+"\n")

    def test_the_answer_is_correct(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        game.places[0] = 3
        actual_result_of_current_category = game._current_category
        game._did_player_win()
        result = game.was_correctly_answered()
        self.assertTrue(game._did_player_win)
        logging.info("The answer is: " + str(result) + "\n")

    

if __name__ == '__main__':
    unittest.main()
