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
#    3.  Texas flag (to determine what play_mode to switch to after come-out roll)
#
#  Returns:
#    1.  Goflag:  0 = end, 1 = keep going
#    2.  Playmode:  Returns the playmode the game should continue in.
#                   N/A If goflag = 0
#
def keep_playing(win_flag, play_mode, texas_flag):  #  Both parameters are mandatory and have no defaults
    """This function looks at both win_flag and play_mode and determines if the player should\n
        asked if they want to continue or not. Assume winning player wants to continue.\n"""
#
    go = 1  #  Constants to make things easier to read
    ask = 0

    if win_flag > 0:  #  Player won at something - therefore restart game if necessary
        return (go, play_mode)  #  Restart using the same play mode
    elif win_flag < 0:  #  Player lost, ask to restart, reset playmode
        play_mode = 0
        return (ask, play_mode)
    elif play_mode == 0:  #  win_flag *MUST* be 0. If play_mode = 0, finished come-out roll
        play_mode = (texas_flag + 1)  #  so we change the play_mode in accordance with texas flag
#                                        (texas_flag = playmode - 1)
        return (go, play_mode)
    else:  #  Both win_flag = 0 *AND* play_mode != 0 - i.e. continue a game in progress
        return (go, play_mode)
#
#  end of function
#