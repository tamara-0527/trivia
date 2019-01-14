#!/usr/bin/python2

import trivia
import unittest
import logging

""" 
In these tests, I tried to test (with unittest) the main methods with return statements.
I used the logging class to make the output of the running test functions more readable and also separate them from each other in some way.
In some assertion methods, I've also used messages, because it can give more information when the test fails. 
In practice, it should be used in each assertions (to make the test output more human-readable and more understandable).
In this test suite there is one test which is failing. This happens because that part of the program code is probably not correct.
Every test has it's own arrange, act and assert sections. I've created a new Game for every test because I would like to make sure they will be independent. 
 """

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class DetailsOfGameTest(unittest.TestCase):
    
    def test_the_players_counter(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        self.assertEqual(game.how_many_players, 2)
        logging.info("Check the numbers of players is counted correctly or not\n")

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

    def test_the_player_is_winner(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        game.places[0] = 3
        game.purses[0] = 7
        winner = game._did_player_win()
        self.assertTrue(winner, game.players[game.current_player] + " should be the winner with " + str(game.purses[game.current_player]) + "\n")
        logging.info("The winner is: " + game.players[game.current_player] + " with " + str(game.purses[game.current_player]) + "\n")
    
    def test_not_winner_with_less_coin(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        game.current_player = 1
        game.places[1] = 3
        game.purses[1] = 5
        winner = game._did_player_win()
        self.assertFalse(winner, "The correct answer should be: " + game.players[game.current_player] + " is not a winner with " + str(game.purses[game.current_player]) + "\n")
    
    def test_not_winner_with_six(self):
        game = trivia.Game()
        game.add('Alex')
        game.add('Kelly')
        game.current_player = 1
        game.places[1] = 3
        game.purses[1] = 6
        winner = game._did_player_win()
        self.assertFalse(winner, "The correct answer should be: " + game.players[game.current_player] + " is not a winner with " + str(game.purses[game.current_player]) + "\n")
        logging.info(game.players[game.current_player] + " is the winner? " + str(winner) + "\n")

if __name__ == '__main__':
    unittest.main()
