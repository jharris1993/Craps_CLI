# Craps_CLI
Command-line version of Vegas Craps

Two basic modes:
1.  "Vegas" style craps with the usual rules.
   a.  "Texas" rules may have to change if I discover
       that what a particular "Texas" rule is actually
       a normal "Vegas" rule.
2.  "Texas" style craps:
   a.  Inherits Vegas rules
   b.  When rolling for your point, both 2 and 7 loose
   c.  Rolling "doubles", (both die show the same number),
       when you make your point wins 2x what your normal
       payout would be.
   d.  (a subset of "c")  If a player looses with snake-
       eyes, (two, a double "1"), don't pass bets win
       2x their payout.

To-do:
1.  Research and expand the rules to approximate "real"
    Vegas-style craps to the greatest extent possible.
2.  Research and make provision for placing "bets".
    Initially this would be simple "pass"/"don't pass"
    betting. (i.e. Betting that the active player will/won't
    make their "point")
   a.  Implement a per-player "bank" which is the total
       amount of money they can play with.  When exhausted
       they can no longer play.
       Note that the "house" will have an inexhaustable bank
       to pay winnings.
   b.  Implement "chips" (i.e. betting in fixed increments)
3.  Research and make provision for placing bets that are
    more exotic than simple pass/don't pass betting
4.  Research and make possible multi-player functionality.
   a.  Multiple players with the dice passing from one
       player to the next.
   b.  Multi-player betting on rolls of the dice, even if
       not their own.

Additional to-do:
1.  Refactor code, (make a new project?), using classes/methods
    instead of function calls.
2.  Research and implement different rule-sets if they exist.
    (i.e. "Atlantic-City", "Monte-Carlo", (etc.) rules.)
3.  Research and implement the possibility of making rule-sets
    pluggable/includable modules that don't require re-factoring
    the code for every rule change.  Maybe this can be a part of
    the first set of to-dos?
