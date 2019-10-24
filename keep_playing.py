#  Keep Playing?
#
#  This routine takes the status of the last round played and determines if the round should
#  automatically continue, or stop and ask the player.
#
#  Rules:
#    1.  If the playmode is 0, (rolling for point):
#        (a)  If the player has *NOT* lost, automatically continue.
#             (i)  If the "Texas" flag is *NOT* set, set playmode = 1
#            (ii)  If the "Texas" flag *IS* set, set playmode = 2
#        (b)  If the player *HAS* lost the come-out roll, ask.
#
#    2.  If the playmode is *NOT* 0, (rolling to make point):
#        (a)  If the player has *NOT* lost: (winflag != -1)
#             (i)  If the player has *NOT* won yet, (winflag = 0),
#                  keep going using the current playmode.
#            (ii)  If the player *HAS* won, (winflag > 0),
#                  keep going and set playmode = 0 (new game)
#        (b)  If the player *HAS* lost, (winflag = -1), ask.
#
#  Ask rules:
#    1.  Ask if the player wishes to continue.
#        (a)  Answer is yes:  Set playmode = 0, (new game), and continue.
#             (i)  "Y", "y", or "", (blank), continues.
#        (b)  Answer is no:  End the game.
#             (i)  "N" or "n" ends the game.
#        (c)  Answer is neither yes nor no:  Repeat the question.
#
#  Dependencies:
#    None
#
#  Parameters:
#    1.  Winflag  (To determine if the game should automatically continue or not.)
#    2.  Playmode (To allow keep_playing to restart the game if necessary.)
#
#  Returns:
#    1.  Goflag:  0 = end, 1 = keep going
#    2.  Playmode:  Returns the playmode the game should continue in.
#                   N/A If goflag = 0
#
def keep_playing(win_flag, play_mode):  #  Both parameters are mandatory and have no defaults
    """This function looks at both win_flag and play_mode and determines if the player should\n
        asked if they want to continue or not. Assume winning player wants to continue.\n"""
#
    go = 1
#    stop = 0

    if play_mode == 0 and win_flag > 0:  #  Player won on the come-out roll
        return (go, play_mode)

